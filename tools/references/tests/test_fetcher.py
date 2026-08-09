"""Reading a whole body, not just its first chunk.

ONE read() IS NOT THE WHOLE BODY. `http.client` serves at most one chunk per
call on a chunked response, so a single `read(cap)` returns whatever the first
chunk held and looks exactly like a complete download. Two conference PDFs were
stored at precisely 1,048,576 bytes - a chunk boundary, not a file size - and
both failed conversion with "does not end with %%EOF".
"""

from . import support  # noqa: F401

import unittest

from refslib import fetcher


class ChunkedStream(object):
    """Answers each read() with at most one chunk, like http.client does."""

    def __init__(self, chunks):
        self.chunks = list(chunks)
        self.asked = []

    def read(self, amount):
        self.asked.append(amount)
        if not self.chunks:
            return b""
        block = self.chunks.pop(0)
        if len(block) > amount:
            self.chunks.insert(0, block[amount:])
            return block[:amount]
        return block


class TestReadingAWholeBody(unittest.TestCase):
    def test_a_chunked_body_is_read_to_the_end(self):
        stream = ChunkedStream([b"A" * 1000, b"B" * 1000, b"C" * 500])
        self.assertEqual(len(fetcher._read_capped(stream, 10 * 1024 * 1024)), 2500)

    def test_the_cap_is_still_a_cap(self):
        stream = ChunkedStream([b"A" * 1000] * 50)
        self.assertEqual(len(fetcher._read_capped(stream, 1500)), 1500)

    def test_a_short_first_chunk_is_not_mistaken_for_the_end(self):
        """The exact failure: the first chunk was a megabyte, the file was
        several, and one read() called it done."""
        stream = ChunkedStream([b"%PDF-" + b"x" * (1024 * 1024 - 5), b"y" * 2048,
                                b"trailer%%EOF"])
        body = fetcher._read_capped(stream, 64 * 1024 * 1024)
        self.assertGreater(len(body), 1024 * 1024)
        self.assertTrue(body.endswith(b"%%EOF"))

    def test_an_empty_read_ends_it(self):
        self.assertEqual(fetcher._read_capped(ChunkedStream([]), 4096), b"")

    def test_nothing_is_requested_past_the_cap(self):
        stream = ChunkedStream([b"A" * 5000])
        fetcher._read_capped(stream, 100)
        self.assertTrue(all(amount <= 100 for amount in stream.asked), stream.asked)


if __name__ == "__main__":
    unittest.main()
