rows = [0]

N = int(input())
for _ in range(N) :
    cow = int(input())
    if rows[-1] == cow :
        continue
    rows.append(cow)

cnt = 0
ans = sorted(rows)
while ans != rows :
    for i in range(2, len(rows)) :
        if rows[i-1] > rows[i] :
            rows[i-1], rows[i] = rows[i], rows[i-1]
            cnt += 1
            
print(cnt)