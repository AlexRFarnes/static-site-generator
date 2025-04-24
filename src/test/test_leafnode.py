import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode(
            "p", 
            "Hello, world!"
        )
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode(
            "a",
            "See more",
            {"href": "https://www.google.com"}
        )
        self.assertEqual(
            node.to_html(),
            "<a href=\"https://www.google.com\">See more</a>"
        )
    
    def test_leaf_no_tag(self):
        node = LeafNode(
            None,
            "Raw text"
        )
        self.assertEqual(
            node.to_html(),
            "Raw text"
        )

    def test_repr(self):
        node = LeafNode(
            "div",
            "Text goes here",
            {"class": "hero"}
        )
        self.assertEqual(
            repr(node),
            "LeafNode(div, Text goes here, {'class': 'hero'})"
        )

if __name__=="__main__":
    unittest.main()