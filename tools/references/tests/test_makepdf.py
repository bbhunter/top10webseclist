"""Turning an archived Markdown file into the HTML that gets printed as a PDF.

This corpus IS exploit research, so the payloads in it are the content: the
converter has to print them faithfully and must never turn one into something a
reader can activate from the archive's own file.
"""

from . import support  # noqa: F401

import unittest

from refslib import makepdf


class TestLinkTargets(unittest.TestCase):
    """A `javascript:` URL in an XSS write-up is ordinary content here. Printed
    as an `<a href>` it becomes a payload the archive itself offers to run."""

    def html(self, markdown):
        return makepdf.markdown_to_html_body(markdown)

    def test_an_http_link_is_printed_as_a_link(self):
        body = self.html("See [the paper](https://example.test/p.pdf).")
        self.assertIn('<a href="https://example.test/p.pdf">the paper</a>', body)

    def test_a_javascript_target_keeps_its_text_and_loses_its_href(self):
        body = self.html("Try [this payload](javascript:alert(1)) in the field.")
        self.assertNotIn("<a", body)
        self.assertIn("this payload", body)

    def test_a_data_url_is_not_printed_as_a_link(self):
        body = self.html("[svg](data:image/svg+xml;base64,PHN2Zz48L3N2Zz4=)")
        self.assertNotIn("<a", body)

    def test_a_query_string_is_escaped_once_and_not_twice(self):
        """`_inline` has already escaped its text, so escaping the target again
        printed `&amp;amp;` and every link with a query string went somewhere
        that does not exist."""
        body = self.html("[report](https://example.test/p?a=1&b=2&c=3)")
        self.assertIn('href="https://example.test/p?a=1&amp;b=2&amp;c=3"', body)
        self.assertNotIn("&amp;amp;", body)

    def test_a_mailto_link_survives(self):
        body = self.html("[report](mailto:security@example.test)")
        self.assertIn('href="mailto:security@example.test"', body)

    def test_an_entity_encoded_scheme_does_not_slip_through(self):
        """The check runs on the unescaped target, because the sink escapes."""
        body = self.html("[x](java&#115;cript:alert(1))")
        self.assertNotIn("<a", body)

    def test_the_payload_text_is_still_readable_in_the_printed_page(self):
        body = self.html("Use `javascript:alert(document.domain)` as the URL.")
        self.assertIn("javascript:alert(document.domain)", body)


if __name__ == "__main__":
    unittest.main()
