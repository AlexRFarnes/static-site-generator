from block_markdown import markdown_to_html_node
from os import path, listdir, makedirs
from pathlib import Path


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    dir_path = Path(dir_path_content)
    dest_path = Path(dest_dir_path)

    for path in listdir(dir_path_content):
        current_path = dir_path.joinpath(path)
        if current_path.is_file():
            name = current_path.stem
            generate_page(current_path, template_path,
                          f"{dest_path}/{name}.html", basepath)
        else:
            new_dest_path = dest_path.joinpath(path)
            generate_pages_recursive(
                current_path, template_path, new_dest_path, basepath)


def generate_page(from_path, template_path, dest_path, basepath):

    print(
        f"Generating page from {from_path} to {dest_path} using {template_path}\n")
    md = None
    template = None
    with open(from_path, "r") as f:
        md = f.read()

    node = markdown_to_html_node(md)
    html = node.to_html()
    title = extract_title(md)

    with open(template_path) as f:
        template = f.read()

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    template = template.replace("href=\"/", f"href=\"{basepath}")
    template = template.replace("src=\"/", f"src=\"{basepath}")

    dest_dir_path = path.dirname(dest_path)
    if dest_dir_path != "":
        makedirs(dest_dir_path, exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(template)


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[1:].strip()
    raise ValueError("h1 header is required")
