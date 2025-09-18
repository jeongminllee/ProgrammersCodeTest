
def calculate(a, b, op) :
    if op == '+' :
        return a + b
    elif op == '-' :
        return a - b
    else :  # op == '*'
        return a * b

def dfs(idx, num) :
    global res

    if idx == N :
        res = max(res, num)
        return

    nxt = calculate(num, int(equation[idx+1]), equation[idx])
    dfs(idx+2, nxt)

    if idx + 4 <= N :
        bracket = calculate(int(equation[idx+1]), int(equation[idx + 3]), equation[idx+2])
        nxt = calculate(num, bracket, equation[idx])
        dfs(idx+4, nxt)

N = int(input())
equation = input()

start = int(equation[0])
res = -1<<32
dfs(1, start)
print(res)