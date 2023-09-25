N, M = map(int, input().split())
box = [0] * N

for _ in range(M) :
    i, j, k = map(int, input().split())
    for idx in range(i, j+1) :
        box[idx - 1] = k
        
for i in range(N) :
    print(box[i], end = ' ')
    