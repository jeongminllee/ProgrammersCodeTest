mat = []
for _ in range(5) :
    mat.append(input())

ans = ''
max_len = 0

for row in mat :
    max_len = max(max_len, len(row))

for i in range(max_len) :
    for row in mat :
        if i < len(row) :
            ans += row[i]

print(ans)