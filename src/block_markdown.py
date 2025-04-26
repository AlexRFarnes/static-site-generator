from enum import Enum
from parentnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    # filter the empty blocks due to excessive newlines
    # and strip any leading or trailing whitespace
    blocks = list(filter(lambda block: block, list(
        map(lambda block: block.strip(), blocks))))
    return blocks


def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING

    if block.startswith("```") and block.endswith("```") and len(lines) > 1:
        return BlockType.CODE

    is_quote = all(line.startswith(">") for line in lines)
    if is_quote:
        return BlockType.QUOTE

    is_unordered_list = all(line.startswith("- ") for line in lines)
    if is_unordered_list:
        return BlockType.UNORDERED_LIST

    is_ordered_list = all(line.startswith(
        f"{i}. ") for i, line in enumerate(lines, 1))
    if is_ordered_list:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html(block)
        children.append(html_node)
    return ParentNode("div", children)


def block_to_html(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html(block)
    if block_type == BlockType.HEADING:
        return heading_to_html(block)
    if block_type == BlockType.CODE:
        return code_to_html(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html(block)
    if block_type == BlockType.UNORDERED_LIST:
        return unordered_list_to_html(block)
    if block_type == BlockType.ORDERED_LIST:
        return ordered_list_to_html(block)
    raise ValueError("invalid block type")


def paragraph_to_html(block):
    lines = " ".join(block.split("\n"))
    return ParentNode("p", text_to_children(lines))


def heading_to_html(block):
    level = block.count("#")
    if level + 1 >= len(block):
        raise ValueError(f"invalid heading level: {level}")
    text = block[level + 1:]
    return ParentNode(f"h{level}", text_to_children(text))


def code_to_html(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    block = block.strip("```").lstrip()
    text_node = TextNode(block, TextType.TEXT)
    html_node = text_node_to_html_node(text_node)
    child = ParentNode("code", [html_node])
    return ParentNode("pre", [child])


def quote_to_html(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    return ParentNode("blockquote", text_to_children(" ".join(new_lines)))


def unordered_list_to_html(block):
    items = block.split("\n")
    list_items = []
    for item in items:
        text = item[2:]
        list_item = ParentNode("li", text_to_children(text))
        list_items.append(list_item)
    return ParentNode("ul", list_items)


def ordered_list_to_html(block):
    items = block.split("\n")
    list_items = []
    for i, item in enumerate(items, 1):
        text = item[3:].lstrip()
        list_item = ParentNode("li", text_to_children(text))
        list_items.append(list_item)
    return ParentNode("ol", list_items)


def text_to_children(text):
    nodes = text_to_textnodes(text)
    children = []
    for node in nodes:
        children.append(text_node_to_html_node(node))
    return children


# def quote_to_html(block):
#     # need to split by \n\n to preserve the inline \n and separate on the empty lines >
#     print("".join(block.split(">")).split("\n\n"))
#     lines = "".join(block.split(">")).split("\n\n")
#     line_elements = []
#     for line in lines:
#         line = line.strip()
#         line = " ".join(line.split("\n"))
#         paragraph = ParentNode("p", text_to_children(line))
#         line_elements.append(paragraph)
#     return ParentNode("blockquote", line_elements)
