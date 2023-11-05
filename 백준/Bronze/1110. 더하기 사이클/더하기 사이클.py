N = int(input())
a = N // 10
b = N % 10
i = 0

while True :
    c = b * 10 + (a + b) % 10
    a = c // 10
    b = c % 10
    i += 1
    if c == N :
        break

print(i)