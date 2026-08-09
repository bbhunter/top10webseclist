"""The explicit, bounded curl fallback used only by recovery commands."""

from . import support  # noqa: F401

import unittest
from unittest import mock

from refslib import fetcher


class TestCurlFallback(unittest.TestCase):
    @mock.patch("refslib.fetcher.shutil.which", return_value="/usr/bin/curl")
    @mock.patch("refslib.fetcher.subprocess.run")
    def test_successful_bytes_become_a_response(self, run, _which):
        run.return_value = mock.Mock(returncode=0, stdout=b"archive bytes", stderr=b"")
        response = fetcher.curl_get("https://archive.test/x", timeout=7, max_bytes=99)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.body, b"archive bytes")
        command = run.call_args.args[0]
        self.assertIn("--max-filesize", command)
        self.assertIn("99", command)

    @mock.patch("refslib.fetcher.shutil.which", return_value=None)
    def test_missing_curl_is_a_network_failure(self, _which):
        self.assertEqual(fetcher.curl_get("https://archive.test/x").status, 0)


if __name__ == "__main__":
    unittest.main()
