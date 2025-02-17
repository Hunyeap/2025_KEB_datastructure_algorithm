def is_even(n) -> bool:
    """
    this function checks if a number is even
    :param n: n is an integer
    :return: if the number is even return True
    """
    if n % 2 == 0:
        return True
    return False
n = int(input())
print(is_even(n))
