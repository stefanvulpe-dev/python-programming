def count_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return len([each for each in text if each.lower() in vowels])


print(count_vowels('foobar'))
