import sys
input = sys.stdin.readline

T = 1000 - int(input())

a, T = divmod(T, 500)
b, T = divmod(T, 100)
c, T = divmod(T, 50)
d, T = divmod(T, 10)
e, T = divmod(T, 5)
f = T

print(sum([a, b, c, d, e, f]))