def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


d = 0
while True:
    n = int(input())
    if n == -1:
        break
    d = gcd(n, d)

print('GCD is: ', d)

