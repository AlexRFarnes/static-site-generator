import re
from textnode import TextType, TextNode


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(
        nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(
        nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        # delimiters should appear in pairs
        if old_node.text.count(delimiter) % 2 != 0:
            raise ValueError(
                "Unmatched delimiter found, invalid Markdwon syntax.")

        split_nodes = []
        split_text = old_node.text.split(delimiter)
        for i, text in enumerate(split_text):
            if text == "":  # Skip empty segments
                continue

            if i % 2 == 0:  # Even index: regular text
                type = TextType.TEXT
            else:  # Odd index: matched text inside delimiters
                type = text_type
            split_nodes.append(TextNode(text, type))

        new_nodes.extend(split_nodes)

    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        # find all matches in the text
        matches = extract_markdown_images(old_node.text)

        if not matches:
            new_nodes.append(old_node)
            continue

        current_text = old_node.text

        for alt_text, url in matches:
            image = f"![{alt_text}]({url})"
            sections = current_text.split(image, 1)

            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")

            # add the text if not empty
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))

            # add the image
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))

            # safety check for when the image markdown is at the end, there is no sections[1] then.
            if len(sections) > 1:
                current_text = sections[1]
            else:
                current_text = ""

        if current_text:
            new_nodes.append(TextNode(current_text, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        matches = extract_markdown_links(old_node.text)

        if not matches:
            new_nodes.append(old_node)
            continue

        current_text = old_node.text

        for text, url in matches:
            link = f"[{text}]({url})"
            sections = current_text.split(link, 1)

            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")

            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))

            new_nodes.append(TextNode(text, TextType.LINK, url))

            if len(sections) > 1:
                current_text = sections[1]
            else:
                current_text = ""

        if current_text:
            new_nodes.append(TextNode(current_text, TextType.TEXT))

        return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

result = text_to_textnodes(text)
for node in result:
    print(node)
