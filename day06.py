def is_even(n) -> bool:
    """
    this function checks if a number is even
    :param n: n is an integer
    :return: if the number is even return True
    """
    return not n & 1 #홀수는 이진수로 표현할 때 마지막이 무조건 1인점을 고안
    # if n % 2 == 0:
    #     return True
    # return False


n = int(input())
print(is_even(n))

# a = 10
# b = 11
# print(a and b)  # different of 'and' and '&'
# print(a & b)
# print(a or b)
# print(a | b)
# print(a ^b)