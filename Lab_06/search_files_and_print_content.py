import os
import sys


def error_handler(exception):
    print('Exception: {}'.format(exception))
    exit(1)


def read_and_print_content(path, extension):
    for (root, _, files) in os.walk(path, onerror=error_handler):
        for file in files:
            if file.endswith(extension):
                try:
                    with open(os.path.join(root, file), 'r') as f:
                        print(f.read())
                except FileNotFoundError:
                    print('FileNotFoundError: {}'.format(os.path.join(root, file)))
                except PermissionError:
                    print('PermissionError: {}'.format(os.path.join(root, file)))
                except IOError:
                    print('IOError: {}'.format(os.path.join(root, file)))
                except Exception as e:
                    print('Exception: {}'.format(e))


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python search_files_and_print_content.py <directory> <extension>')
        exit(1)
    directory = sys.argv[1]
    extension = sys.argv[2]
    valid_extensions = ['txt', 'py', 'md', 'html', 'css', 'js']
    if extension not in valid_extensions:
        print('Invalid extension. Valid extensions are: {}'.format(', '.join(valid_extensions)))
        exit(1)
    read_and_print_content(directory, extension)
