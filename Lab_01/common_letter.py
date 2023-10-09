def most_common_letter(text):
    frequencies = {}
    for letter in text.lower():
        if letter.isalpha():
            if letter not in frequencies:
                frequencies[letter] = 0
            frequencies[letter] += 1

    best_letter = None
    best_count = 0
    for letter, count in frequencies.items():
        if not best_letter or count > best_count:
            best_letter = letter
            best_count = count
    return best_letter, best_count


print(most_common_letter("An apple is not a tomato"))
