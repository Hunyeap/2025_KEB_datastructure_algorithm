def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def nCr(n, r) -> int :
    numerator = factorial(n)
    denominator = factorial(r) * factorial(n - r)
    return int (numerator / denominator)

# n = int(input())
# r = int(input())
# print(nCr(n, r))

def octal_number(n):
    """
    This function returns the octal number
    :param n: number to calculate octal number
    :return: octal number
    """
    if n == 0:
        return 0
    else :
        return octal_number(n // 8) * 10  + (n % 8)


c = int(input())
print(octal_number(c))
