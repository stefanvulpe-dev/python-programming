# Ex. 1
def first_fibonacci_numbers(n):
    a, b = 0, 1
    res = []
    for i in range(n):
        res.append(a + b)
        a, b = b, a + b
    return res


print(first_fibonacci_numbers(10))


# Ex. 2
def is_prime(x):
    if x == 0 or x == 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(x ** 0.5), 2):
        if x % i == 0:
            return False
    return True


def find_primes(numbers):
    return list(filter(is_prime, numbers))


print(find_primes(range(100)))


# Ex. 3
def set_operations(a, b):
    intersection = [x for x in a if x in b]
    union = [x for x in a if x not in b] + b
    a_minus_b = [x for x in a if x not in b]
    b_minus_a = [x for x in b if x not in a]
    return intersection, union, a_minus_b, b_minus_a


print(set_operations([1, 2, 3], [2, 3, 4]))


# Ex. 4
def compose(notes, moves, start):
    res = [notes[start]]
    for move in moves:
        start += move
        if start > len(notes) - 1:
            start = start - len(notes)
        res.append(notes[start])
    return res


print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))


# Ex. 5
def replace_under_main_diagonal(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i > j:
                matrix[i][j] = 0
    return matrix


print(replace_under_main_diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


# Ex. 6
def repeated_occurrences(*lists, x):
    freq = {}
    for lst in lists:
        for item in lst:
            if item not in freq:
                freq[item] = 1
            else:
                freq[item] += 1
    res = []
    for k, v in freq.items():
        if v == x:
            res.append(k)
    return res


print(repeated_occurrences([1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"], x=2))


# Ex. 7
def palindrome_tuple(lst):
    res = []
    for item in lst:
        if str(item) == str(item)[::-1]:
            res.append(item)
    return len(res), max(res)


print(palindrome_tuple([11, 35, 46, 17, 19, 22]))


# Ex. 8
def ascii_codes(strings, flag=True, x=1):
    res = []
    for string in strings:
        if flag:
            res.append([letter for letter in string if ord(letter) % x == 0])
        else:
            res.append([letter for letter in string if ord(letter) % x != 0])
    return res


print(ascii_codes(["test", "hello", "lab002"], flag=False, x=2))


# Ex. 9
def taller_spectators(matrix):
    res = []
    for i in range(1, len(matrix)):
        for k in range(i):
            for j in range(len(matrix[0])):
                if matrix[i][j] <= matrix[k][j] and (i, j) not in res:
                    res.append((i, j))
    return res


print(taller_spectators([[1, 2, 3, 2, 1, 1], [2, 4, 4, 3, 7, 2], [5, 5, 2, 5, 6, 4], [6, 6, 7, 6, 7, 5]]))


# Ex. 10
def tuples_from_lists(*lists):
    return list(zip(*lists))


print(tuples_from_lists([1, 2, 3], [5, 6, 7], ["a", "b", "c"]))


# Ex. 11
def order_tuples(lst):
    return sorted(lst, key=lambda x: x[1][2])


print(order_tuples([('abc', 'bcd'), ('abc', 'zza')]))


# Ex. 12
def group_by_rhyme(words):
    rhymes = []
    while len(words) > 0:
        word = words[0]
        res = filter(lambda x: x.endswith(word[-2:]), words)
        rhymes.append(list(res))
        words = list(filter(lambda x: not x.endswith(word[-2:]), words))
    return rhymes


print(group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))
