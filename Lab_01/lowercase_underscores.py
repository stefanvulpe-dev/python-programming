def convert_lower_snake(text):
    last_camel = 0
    new_str = ''
    for i in range(len(text)):
        if text[i].isupper():
            if i != 0:
                new_str += text[last_camel:i].lower() + '_'
            last_camel = i
    new_str += text[last_camel:].lower()
    return new_str


print(convert_lower_snake('UpperCamelCase'))
