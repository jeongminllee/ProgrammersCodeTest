N, M = map(int, input().split())
box = [n for n in range(1, N + 1)]
temp = 0

for i in range(M) :
    i, j = map(int, input().split())
    temp = box[i-1]
    box[i-1] = box[j-1]
    box[j-1] = temp
    
for i in range(N) :
    print(box[i], end = ' ')
    