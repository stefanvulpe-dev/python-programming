def words_counter(text):
    frequencies = {}
    for word in text.lower().split(' '):
        if word not in frequencies:
            frequencies[word] = 1
        else:
            frequencies[word] += 1

    return len(frequencies)


print(words_counter("I have Python exam on Monday. I have to study. I have to study. I have to study."))
