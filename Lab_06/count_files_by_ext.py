import os
import sys


def error_handler(exception):
    print('Exception: {}'.format(exception))
    exit(1)


def count_files(path):
    extensions = {}
    for (root, _, files) in os.walk(path, onerror=error_handler):
        for file in files:
            try:
                file_ext = os.path.splitext(file)[1] or os.path.splitext(file)[0]
                extensions[file_ext] = extensions.get(file_ext, 0) + 1
            except FileNotFoundError:
                print('FileNotFoundError: {}'.format(os.path.join(root, file)))
            except PermissionError:
                print('PermissionError: {}'.format(os.path.join(root, file)))
            except Exception as e:
                print('Exception: {}'.format(e))
    return extensions


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python count_files_by_ext.py <directory>')
        exit(1)
    print(count_files(sys.argv[1]))
