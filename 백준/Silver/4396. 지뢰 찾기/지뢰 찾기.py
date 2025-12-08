import copy

di = [-1, -1, -1, 0, 0, 1, 1, 1]
dj = [-1, 0, 1, -1, 1, -1, 0, 1]

def check(si:int, sj:int, arr:list[list[str]], users_arr:list[list[str]]) :
    n = len(res)
    cnt = 0

    ci = si
    cj = sj

    for d in range(8) :
        ni, nj = ci + di[d], cj + dj[d]
        if 0<=ni<n and 0<=nj<n :
            if arr[ni][nj] == "." :
                continue
            elif arr[ni][nj] == "*" :
                cnt += 1

    res[si][sj] = str(cnt)

def main() :
    global res
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    users_arr = [list(input()) for _ in range(n)]

    res = [["."] * n for _ in range(n)]

    for i in range(n) :
        for j in range(n) :
            if users_arr[i][j] == "x" and arr[i][j] == "*" :    # 지뢰를 밟았으면
                res = copy.deepcopy(arr)
                break

    for i in range(n) :
        for j in range(n) :
            if users_arr[i][j] == "x" and res[i][j] != "*":
                check(i, j, arr, users_arr)

    for i in range(n) :
        print("".join(res[i]))

if __name__ == "__main__" :
    main()