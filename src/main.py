from os import path, getcwd
from generate_page import generate_page, generate_static_dir


def main():
    cwd = getcwd()
    from_path = path.join(cwd, "static")
    dest_path = path.join(cwd, "public")
    template_path = path.join(cwd, "template.html")
    md_path = path.join(cwd, "content", "index.md")
    index_path = path.join(dest_path, "index.html")

    generate_static_dir(from_path, dest_path)
    generate_page(md_path, template_path, index_path)


if __name__ == "__main__":
    main()
