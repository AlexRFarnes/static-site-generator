from pathlib import Path
from generate_page import generate_pages_recursive
from generate_static import generate_static_files


def main():
    from_path = Path.cwd().joinpath("static")
    dest_path = Path.cwd().joinpath("public")
    template_path = Path.cwd().joinpath("template.html")
    dir_path_content = Path.cwd().joinpath("content")

    print("Copying the static files to the public directory...")
    generate_static_files(from_path, dest_path)
    # generate_page(md_path, template_path, index_path)
    print("Generating the pages...")
    generate_pages_recursive(dir_path_content, template_path, dest_path)


if __name__ == "__main__":
    main()
