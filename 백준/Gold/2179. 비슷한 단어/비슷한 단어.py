def check(x, y) :
    cnt = 0
    mn_len = min(len(x), len(y))
    for i in range(mn_len) :
        if x[i] == y[i] :
            cnt += 1
        else :
            return cnt

    return cnt

N = int(input())
S = [input() for _ in range(N)]
mx_len = [-1, -1, 0]

for x in range(N) :
    for y in range(x+1, N) :
        cur = check(S[x], S[y])
        if mx_len[2] < cur :
            mx_len[0] = x
            mx_len[1] = y
            mx_len[2] = cur

print(S[mx_len[0]])
print(S[mx_len[1]])