from textnode import TextNode, TextType
from shutil import rmtree, copy
from os import path, listdir, mkdir, getcwd


def main():
    generate_static()


def generate_static():
    cwd = getcwd()
    dest_path = path.join(cwd, "public")
    src_path = path.join(cwd, "static", )

    if path.exists(dest_path):
        rmtree(dest_path)
    mkdir(dest_path)

    all_paths = get_list_of_paths(src_path, dest_path)

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


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[1:].strip()
    raise ValueError("h1 header is required")


if __name__ == "__main__":
    main()
