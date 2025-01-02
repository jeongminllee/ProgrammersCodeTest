import copy

def left(arr) :
    for i in range(N) :
        cursor = 0
        for j in range(1, N) :
            if arr[i][j] != 0 :
                tmp = arr[i][j]
                arr[i][j] = 0

                if arr[i][cursor] == 0 :
                    arr[i][cursor] = tmp

                elif arr[i][cursor] == tmp :
                    arr[i][cursor] *= 2
                    cursor += 1

                else :
                    cursor += 1
                    arr[i][cursor] = tmp

    return arr

def right(arr) :
    for i in range(N) :
        cursor = N - 1
        for j in range(N - 1, -1, -1) :
            if arr[i][j] != 0 :
                tmp = arr[i][j]
                arr[i][j] = 0

                if arr[i][cursor] == 0 :
                    arr[i][cursor] = tmp

                elif arr[i][cursor] == tmp :
                    arr[i][cursor] *= 2
                    cursor -= 1

                else :
                    cursor -= 1
                    arr[i][cursor] = tmp

    return arr

def up(arr) :
    for j in range(N) :
        cursor = 0
        for i in range(N) :
            if arr[i][j] != 0 :
                tmp = arr[i][j]
                arr[i][j] = 0

                if arr[cursor][j] == 0 :
                    arr[cursor][j] = tmp

                elif arr[cursor][j] == tmp :
                    arr[cursor][j] *= 2
                    cursor += 1

                else :
                    cursor += 1
                    arr[cursor][j] = tmp

    return arr

def down(arr) :
    for j in range(N) :
        cursor = N - 1
        for i in range(N - 1, -1, -1) :
            if arr[i][j] != 0 :
                tmp = arr[i][j]
                arr[i][j] = 0

                if arr[cursor][j] == 0 :
                    arr[cursor][j] = tmp

                elif arr[cursor][j] == tmp :
                    arr[cursor][j] *= 2
                    cursor -= 1

                else :
                    cursor -= 1
                    arr[cursor][j] = tmp

    return arr


def dfs(n, arr) :
    global ans
    if n == 5 :
        for i in range(N) :
            for j in range(N) :
                if arr[i][j] > ans :
                    ans = arr[i][j]
        return

    for i in range(4) :
        copy_arr = copy.deepcopy(arr)
        if i == 0 :
            dfs(n + 1, left(copy_arr))
        elif i == 1:
            dfs(n + 1, right(copy_arr))
        elif i == 2:
            dfs(n + 1, up(copy_arr))
        else :
            dfs(n + 1, down(copy_arr))

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
dfs(0, arr)

print(ans)