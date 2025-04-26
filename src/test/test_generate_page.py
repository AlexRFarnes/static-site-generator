import unittest
from generate_page import extract_title


class TestGeneratePage(unittest.TestCase):
    def test_extract_title(self):
        md = """
# Title 1

Some random text
"""
        title = extract_title(md)
        self.assertEqual(title, "Title 1")

    def test_missing_title(self):
        md = """
## Level 2 heading

A paragraph and nothing more
"""
        self.assertRaises(ValueError, extract_title, md)


if __name__ == "__main__":
    unittest.main()
