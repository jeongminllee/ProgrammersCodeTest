N = int(input())
arr = [[0] * 102 for _ in range(102)]
for _ in range(N) :
    # [1] 해당 영역을 1로 표시
    sj, si = map(int, input().split())
    for i in range(si, si + 10) :
        for j in range(sj, sj + 10) :
            arr[i][j] = 1

    # [2] 1의 개수를 춧 => 넓이
    ans = 0
    for lst in arr :
         ans += sum(lst)

print(ans)