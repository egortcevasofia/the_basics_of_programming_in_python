def fastPow(a, n):
    def even(n):
        if n % 2 == 0:
            return 1
        return 0
    if n == 0:
        return 1
    if even(n):
        return fastPow(a, n / 2) ** 2
    return a * fastPow(a, n - 1)

a = float(input())
n = float(input())
print(fastPow(a, n))
