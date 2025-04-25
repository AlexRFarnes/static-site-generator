from enum import Enum


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
    split_lines = block.split("\n")
    # regex ^#{1,6}\s.
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING

    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    is_quote = all(line.startswith(">") for line in split_lines)
    if is_quote:
        return BlockType.QUOTE

    is_unordered_list = all(line.startswith("- ") for line in split_lines)
    if is_unordered_list:
        return BlockType.UNORDERED_LIST

    is_ordered_list = all(line.startswith(
        f"{i + 1}. ") for i, line in enumerate(split_lines))
    if is_ordered_list:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH


print(block_to_block_type("# Heading"))
print(block_to_block_type("###### Heading"))
print(block_to_block_type("####### Heading 7"))
print(block_to_block_type("```This is some code```"))
print(block_to_block_type("```This is not code``"))
print(block_to_block_type(
    "> This is the first list item in a quote block\n> This is a quote item\n> This is another quote item"))
print(block_to_block_type(
    "- This is the first list item in a list block\n- This is a list item\n- This is another list item"))
print(block_to_block_type(
    "1. This is the first list item in a list block\n2. This is a list item\n3. This is another list item"))
print(block_to_block_type(
    "1. This is the first list item in a list block\n3. This is a list item\n4. This is another list item"))
print(block_to_block_type(
    "5. This is the first list item in a list block\n6. This is a list item\n7. This is another list item"))
