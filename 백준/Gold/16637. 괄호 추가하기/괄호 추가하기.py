# 연산자 우선순위가 모두 동일함.
# 괄호 안에 연산자는 하나만 들어갈 수 있고
# 괄호의 수 제한은 없다. 0이어도 되고 가능한 다 해도 된다.

def calculate(a, b, op) :
    if op == '+' :
        return a + b
    elif op == '-' :
        return a - b
    elif op == '*' :
        return a * b

def dfs(idx, curr) :
    global res

    if idx == N :
        res = max(res, curr)
        return

    nxt = calculate(curr, int(equation[idx + 1]), equation[idx])
    dfs(idx + 2, nxt)

    if idx + 4 <= N :
        bracket = calculate(int(equation[idx + 1]), int(equation[idx + 3]), equation[idx + 2])
        nxt = calculate(curr, bracket, equation[idx])
        dfs(idx + 4, nxt)

N = int(input())
equation = input()
res = -1 << 32
dfs(1, int(equation[0]))
print(res)