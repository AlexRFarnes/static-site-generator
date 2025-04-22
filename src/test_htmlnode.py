import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_values(self):
        node = HTMLNode(
            "p",
            "Random text",
            None,
            {"class": "heading"}
        )
        self.assertEqual(
            node.tag, 
            "p"
            )
        self.assertEqual(
            node.value,
            "Random text"
        )
        self.assertEqual(
            node.children,
            None
        )
        self.assertEqual(
            node.props,
            {"class": "heading"}
        )

    def test_props_to_html(self):
        node = HTMLNode(
            "a",
            "More info",
            None,
            {"href": "https://www.google.com", "target": "_blank", "class": "cta"}
        )
        self.assertEqual(
            node.props_to_html(), 
            ' href="https://www.google.com" target="_blank" class="cta"'
        )

    def test_repr(self):
        node = HTMLNode(
            "div", 
            "Some text", 
            None, 
            {"style": "background-color=\"blue\"", "class": "subtitle"})
        self.assertEqual(
            repr(node), 
            "HTMLNode(div, Some text, children: None, {'style': 'background-color=\"blue\"', 'class': 'subtitle'})"
        )


if __name__=="__main__":
    unittest.main()