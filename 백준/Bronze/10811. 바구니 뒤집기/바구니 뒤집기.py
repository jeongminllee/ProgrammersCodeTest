N, M = map(int, input().split())

box = [n for n in range(1, N + 1)]

for _ in range(M) :
    a, b = map(int, input().split())
    temp = box[a-1 : b]
    temp.reverse()
    box[a-1 : b] = temp
    
for i in range(N) :
    print(box[i], end = " ")