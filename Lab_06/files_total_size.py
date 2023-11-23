import os
import sys


def err_handler(exception):
    print("Exception: {}".format(exception))


def calculate_total_size(path):
    total_size = 0
    for (root, _, files) in os.walk(path, onerror=err_handler):
        for file in files:
            try:
                file_path = os.path.join(root, file)
                total_size += os.path.getsize(file_path)
            except FileNotFoundError:
                print('FileNotFoundError: {}'.format(os.path.join(root, file)))
            except PermissionError:
                print('PermissionError: {}'.format(os.path.join(root, file)))
            except Exception as e:
                print('Exception: {}'.format(e))
    return total_size


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python files_total_size.py <directory>')
        exit(1)
    print('Total size: {} bytes'.format(calculate_total_size(sys.argv[1])))
    