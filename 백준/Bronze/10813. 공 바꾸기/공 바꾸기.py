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


# n, m = map(int, input().split())
# s = [i for i in range(1, n+1)]
# for _ in range(m):
#     a, b = map(int, input().split())
#     s[a-1], s[b-1] = s[b-1], s[a-1]
# print(*s)
