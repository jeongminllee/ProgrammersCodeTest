X = int(input())
n = 1

while X > n :
    X -= n
    n += 1

# 짝수일 경우
if n % 2 == 0 :
    a = X
    b = n - X + 1

# 홀수일 경우
else :
    a = n - X + 1
    b = X

print(f"{a}/{b}")