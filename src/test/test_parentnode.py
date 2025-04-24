import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("bold", "child")
        parent_node = ParentNode("p", [child_node])
        self.assertEqual(parent_node.to_html(), "<p><bold>child</bold></p>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("span", "grandchild")
        child_node = ParentNode("p", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><p><span>grandchild</span></p></div>")

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                ]
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
    
    def test_exception_no_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        self.assertRaises(ValueError, parent_node.to_html)

    def test_exception_no_children(self):
        parent_node = ParentNode("p", None)
        self.assertRaises(ValueError, parent_node.to_html)

if __name__ == "__main__":
    unittest.main()
