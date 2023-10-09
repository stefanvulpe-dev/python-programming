import re


def extract_number(text):
    match = re.search(r'(0|[1-9]\d*)', text)
    if match:
        return match.group(0)
    return None


print(extract_number('hello0123'))
