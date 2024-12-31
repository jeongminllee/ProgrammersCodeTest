N = int(input())
graph = [[0] * 58 for _ in range(58)]
X = 0
for _ in range(N) :
    left, right = input().split(' => ')
    if left == right :
        continue
    P = ord(left) - 65
    Q = ord(right) - 65
    if graph[P][Q] == 0 :
        graph[P][Q] = 1
        X += 1

for k in range(58) :
    for i in range(58) :
        for j in range(58):
            if i != j and not graph[i][j] and graph[i][k] and graph[k][j] :
                graph[i][j] = 1
                X += 1

print(X)
for i in range(58) :
    for j in range(58) :
        if i == j :
            continue
        if graph[i][j] :
            print(f'{chr(i + 65)} => {chr(j + 65)}')