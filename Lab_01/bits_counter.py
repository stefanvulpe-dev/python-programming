def bits_counter(x):
    count = 0
    while x:
        count += x & 1
        x >>= 1
    return count


print(bits_counter(24))
