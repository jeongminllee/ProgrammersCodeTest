N, X = map(int, input().split())
A = list(map(int, input().split()))
x_list = []

for i, val in enumerate(A) :
    if val < X :
        print(val, end=" ")