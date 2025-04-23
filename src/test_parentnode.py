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


if __name__ == "__main__":
    unittest.main()
