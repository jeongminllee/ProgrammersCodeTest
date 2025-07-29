D = int(input())
MOD = 1_000_000_007

edges = [[0] * 8 for _ in range(8)]
edges[0][1] = edges[0][2] = 1
edges[1][0] = edges[1][2] = edges[1][3] = 1
edges[2][0] = edges[2][1] = edges[2][3] = edges[2][4] = 1
edges[3][1] = edges[3][2] = edges[3][4] = edges[3][5] = 1
edges[4][2] = edges[4][3] = edges[4][5] = edges[4][7] = 1
edges[5][3] = edges[5][4] = edges[5][6] = 1
edges[6][5] = edges[6][7] = 1
edges[7][4] = edges[7][6] = 1

def multiply(A, B) :
    res = [[0] * 8 for i in range(8)]
    for i in range(8) :
        for j in range(8) :
            for k in range(8) :
                res[i][j] += A[i][k] * B[k][j]
            res[i][j] %= MOD
    return res

def cal(A, n) :
    if n == 1 :
        return A
    cal2 = cal(A, n // 2)
    if n % 2 == 0 :
        return multiply(cal2, cal2)
    else :
        return multiply(multiply(cal2, cal2), A)
res = cal(edges, D)
print(res[0][0])