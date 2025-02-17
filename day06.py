n = int(input())
def sum(n):
    if n % 2 == 0:
        return int((1 + n) * (n/2))

    else:
        return int(((n + 1) * ((n-1)/2)) + ((n+1)/2))

print(sum(n))

r = 0
for i in range(n+1):
    r = r + i
print(r)