def palindrome(num):
    return str(num) == str(num)[::-1]


print(palindrome(110))