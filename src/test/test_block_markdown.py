import unittest
from block_markdown import markdown_to_blocks, block_to_block_type, BlockType, markdown_to_html_node


class TestBlockMarkdown(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_heading_level_1_block(self):
        md = "# Heading 1"
        self.assertEqual(block_to_block_type(md), BlockType.HEADING)

    def test_heading_level_6_block(self):
        md = "###### Heading"
        self.assertEqual(block_to_block_type(md), BlockType.HEADING)

    def test_invalid_heading_block(self):
        md = "####### Heading"
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)

    def test_paragraph_block(self):
        md = "This is a regular paragraph"
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)

    def test_code_block(self):
        md = "```\nThis is a block of code\n```"
        self.assertEqual(block_to_block_type(md), BlockType.CODE)

    def test_invalid_code_block(self):
        md = "```\nThis is not a valid code block\n``"
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)

    def test_quote_block(self):
        md = "> This is the first list item in a quote block\n> This is a quote item\n> This is another quote item"
        self.assertEqual(block_to_block_type(md), BlockType.QUOTE)

    def test_unordered_list_block(self):
        md = "- This is the first list item in a list block\n- This is a list item\n- This is another list item"
        self.assertEqual(block_to_block_type(md), BlockType.UNORDERED_LIST)

    def test_ordered_list_block(self):
        md = "1. This is the first list item in a list block\n2. This is a list item\n3. This is another list item"
        self.assertEqual(block_to_block_type(md), BlockType.ORDERED_LIST)

    def test_invalid_ordered_list_block(self):
        md = "1. This is the first list item in a list block\n3. This is a list item\n4. This is another list item"
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)

    def test_invalid_ordered_list_block_2(self):
        md = "5. This is the first list item in a list block\n6. This is a list item\n7. This is another list item"
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)

    def test_headings(self):
        md = """
# cool h1

paragraph

## cool h2
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>cool h1</h1><p>paragraph</p><h2>cool h2</h2></div>"
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_blockquote(self):
        md = """
> This is a blockquote
> with multiple lines in the same paragraph
> 
> This is a second paragraph in the blockquote

Paragraph
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote><p>This is a blockquote with multiple lines in the same paragraph</p><p>This is a second paragraph in the blockquote</p></blockquote><p>Paragraph</p></div>",
        )

    def test_unordered_list(self):
        md = """
- Item 1
- Item 2
- Item 3
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul></div>"
        )

    def test_ordered_list(self):
        md = """
1. Item 1
2. Item 2
3. Item 3
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>Item 1</li><li>Item 2</li><li>Item 3</li></ol></div>"
        )


if __name__ == "__main__":
    unittest.main()
