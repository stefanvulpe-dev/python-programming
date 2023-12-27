# Ex 1
def set_operations(a, b):
    a_set = set(a)
    b_set = set(b)
    return [a_set & b_set, a_set | b_set, a_set - b_set, b_set - a_set]


print(set_operations([1, 2, 3], [2, 3, 4]))


# Ex 2
def dict_from_string(string):
    string = string.replace(' ', '')
    return dict(zip(string, [string.count(i) for i in string]))


print(dict_from_string('Anna has apples'))


# Ex 3
def compare_dicts(dict1, dict2):
    if type(dict1) is dict and type(dict2) is dict:
        if len(dict1) != len(dict2):
            return False
        for key in dict1:
            if key not in dict2 or not compare_dicts(dict1[key], dict2[key]):
                return False
        return True
    elif type(dict1) is list and type(dict2) is list:
        if len(dict1) != len(dict2):
            return False
        for item1, item2 in zip(sorted(dict1), sorted(dict2)):
            if not compare_dicts(item1, item2):
                return False
        return True
    elif type(dict1) is set and type(dict2) is set:
        return dict1 == dict2
    else:
        return dict1 == dict2


d1 = {'key1': {'key2': [1, 2]}, 'key3': 3}
d2 = {'key3': 3, 'key1': {'key2': [1, 2]}}
print(compare_dicts(d1, d2))  # returns True


# Ex 4
def build_xml(tag, content, **attrs):
    attrs_str = ''
    for attr in attrs:
        attrs_str += f' {attr}="{attrs[attr]}"'
    return f'<{tag}{attrs_str}>{content}</{tag}>'


print(build_xml('a', 'Hello World!', href='https://python.org', _class="my-link", id="some_id"))


# Ex 5
def is_in_middle(string, substring):
    if substring == '':
        return True
    else:
        return string.find(substring) != -1 and string.find(substring) != 0 and string.find(substring) != len(
            string) - 1


def validate_dict(rules, dictionary: {str: str}):
    for rule in rules:
        key = rule[0]
        if key not in dictionary:
            return False
        if not dictionary[key].startswith(rule[1]):
            return False
        if not is_in_middle(dictionary[key], rule[2]):
            return False
        if not dictionary[key].endswith(rule[3]):
            return False
    return True


print(validate_dict({("key1", "", "inside", ""), ("key2", "start", "middle", "winter"), ("key3", "ana", "ana", "ana")},
                    {"key1": "come inside, it's too cold out", "key2": "start, middle, winter",
                     "key3": "ana"}))  # returns False because of key3


# Ex 6
def list_stats(lst):
    return 2 * len(set(lst)) - len(lst), len(lst) - len(set(lst))


print(list_stats([1, 2, 3, 4, 4, 5, 6, 1, 2, 3, 7, 8, 9, 10]))


# Ex 7
def multiple_set_operations(*sets):
    d = {}
    for i in range(len(sets) - 1):
        for j in range(i + 1, len(sets)):
            d["{} | {}".format(sets[i], sets[j])] = sets[i] | sets[j]
            d["{} & {}".format(sets[i], sets[j])] = sets[i] & sets[j]
            d["{} - {}".format(sets[i], sets[j])] = sets[i] - sets[j]
            d["{} - {}".format(sets[j], sets[i])] = sets[j] - sets[i]
    return d


print(multiple_set_operations({1, 2, 3}, {2, 3, 4}, {3, 4, 5}))


# Ex 8
def loop_over_dict_keys(dictionary):
    visited = []
    res = []
    current_key = 'start'
    while True:
        if current_key in visited:
            break
        visited.append(current_key)
        res.append(dictionary[current_key])
        current_key = dictionary[current_key]
    return res


print(loop_over_dict_keys({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))


# Ex 9
def my_function(*args, **kwargs):
    count = 0
    for arg in args:
        if arg in kwargs.values():
            count += 1
    return count


print(my_function(1, 2, 3, 4, 5, a=2, b=3, c=6, d=5))
