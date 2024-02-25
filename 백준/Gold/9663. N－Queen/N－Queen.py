def check(n) :
    for i in range(n) :
        if row[n] == row[i] or abs(row[n] - row[i]) == n - i :
            return False
    return True

def solve(n) :
    global result
    if n == N :
        result += 1
    else :
        for i in range(N) :
            row[n] = i
            if check(n) :
                solve(n + 1)
                
N = int(input())
row = [0] * N
result = 0
solve(0)
print(result)