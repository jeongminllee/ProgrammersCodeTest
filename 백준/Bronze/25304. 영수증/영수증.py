X = int(input())
N = int(input())
s = 0
for i in range(N) :
    a, b = map(int, input().split())
    s += a * b
if s == X :
    print('Yes')
else :
    print("No")    