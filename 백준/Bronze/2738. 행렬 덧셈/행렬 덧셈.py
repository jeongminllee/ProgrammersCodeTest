N, M = map(int, input().split())
matrix1 = []
matrix2 = []
res = [[0] * M for _ in range(N)]

for i in range(N) :
    matrix1.append(list(map(int, input().split())))
for i in range(N) :
    matrix2.append(list(map(int, input().split())))

for i in range(N) :
    for j in range(M) :
        res[i][j] = matrix1[i][j] + matrix2[i][j]

for r in res :
    print(*r)