import os
import sys


def error_handler(exception):
    print('Exception: {}'.format(exception))
    exit(1)


def rename_files_with_common_ext(path):
    for (root, _, files) in os.walk(path, onerror=error_handler):
        extensions = {}
        for file in files:
            try:
                file_path = os.path.join(root, file)
                file_ext = os.path.splitext(file)[1]
                extensions[file_ext] = extensions.get(file_ext, 0) + 1
                new_file_path = os.path.join(root, f"file{extensions[file_ext]}{file_ext}")
                os.rename(file_path, new_file_path)
            except FileNotFoundError:
                print('FileNotFoundError: {}'.format(os.path.join(root, file)))
            except PermissionError:
                print('PermissionError: {}'.format(os.path.join(root, file)))
            except Exception as e:
                print('Exception: {}'.format(e))


def rename_files(path):
    for (root, _, files) in os.walk(path, onerror=error_handler):
        for index, file in enumerate(files):
            try:
                file_path = os.path.join(root, file)
                file_name = os.path.splitext(file)[0]
                os.rename(file_path, file_path.replace(file_name, f"{file_name}{str(index)}"))
            except FileNotFoundError:
                print('FileNotFoundError: {}'.format(os.path.join(root, file)))
            except PermissionError:
                print('PermissionError: {}'.format(os.path.join(root, file)))
            except Exception as e:
                print('Exception: {}'.format(e))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python rename_files.py <directory>')
        exit(1)
    # indiferent de extensie, in ordinea naturala in care apar fisierele in director
    # rename_files(sys.argv[1])
    # redenumesc fisierele care au aceeasi extensie, varianta mai intuitiva din exemplu
    rename_files_with_common_ext(sys.argv[1])
    