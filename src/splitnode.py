from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        if old_node.text.count(delimiter) % 2 != 0: # delimiters should appear in pairs
            raise ValueError("Unmatched delimiter found, invalid Markdwon syntax.")
        
        split_nodes = []
        split_text = old_node.text.split(delimiter)
        for i, text in enumerate(split_text):
            if text == "":  # Skip empty segments
                continue

            if i % 2 == 0: # Even index: regular text
                type = TextType.TEXT
            else:  # Odd index: matched text inside delimiters
                type = text_type
            split_nodes.append(TextNode(text, type))

        new_nodes.extend(split_nodes)

    return new_nodes   

