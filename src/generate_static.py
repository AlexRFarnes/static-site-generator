from shutil import rmtree, copy
from os import path, listdir, mkdir


def generate_static_files(from_path, dest_path):

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
