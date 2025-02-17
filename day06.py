def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def nCr(n, r) -> int :
    numerator = factorial(n)
    denominator = factorial(r) * factorial(n - r)
    return int (numerator / denominator)

n = int(input())
r = int(input())
print(nCr(n, r))
