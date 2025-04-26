from block_markdown import markdown_to_html_node
from shutil import rmtree, copy
from os import path, listdir, mkdir, getcwd


def generate_page(from_path, template_path, dest_path):

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

    lines = template.split("\n")
    new_lines = []
    for line in lines:
        if "{{ Title }}" in line:
            sections = line.split("{{ Title }}")
            line = "".join(sections[0] + title + sections[1])

        if "{{ Content }}" in line:
            sections = line.split("{{ Content }}")
            line = "".join(sections[0] + html + sections[1])
        new_lines.append(line)
    template = "\n".join(new_lines)

    with open(dest_path, "w") as f:
        f.write(template)


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[1:].strip()
    raise ValueError("h1 header is required")


def generate_static_dir(from_path, dest_path):

    if path.exists(dest_path):
        rmtree(dest_path)
    mkdir(dest_path)

    all_paths = get_list_of_paths(from_path, dest_path)

    for src, dst in all_paths:
        if not path.isfile(src):
            mkdir(dst)
        else:
            copy(src, dst)


def get_list_of_paths(src, dst):
    list_files = []
    for file in listdir(src):
        src_path = path.join(src, file)
        dst_path = path.join(dst, file)
        if path.isfile(src_path):
            list_files.append((src_path, dst_path))
        else:
            list_files.append((src_path, dst_path))
            list_files.extend(get_list_of_paths(src_path, dst_path))
    return list_files
