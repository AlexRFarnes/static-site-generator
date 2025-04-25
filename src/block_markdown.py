def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    # filter the empty blocks due to excessive newlines
    # and strip any leading or trailing whitespace
    blocks = list(filter(lambda block: block, list(
        map(lambda block: block.strip(), blocks))))

    return blocks
