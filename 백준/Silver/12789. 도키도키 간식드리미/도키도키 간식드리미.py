def snacks(n, numbers) :
    stack = []
    cnt = 1

    for num in numbers :
        while stack and stack[-1] == cnt :
            stack.pop()
            cnt += 1
        if num == cnt :
            cnt += 1
        else :
            stack.append(num)

    while stack :
        if stack.pop() != cnt :
            return "Sad"
        cnt += 1

    return "Nice"

N = int(input())
stu = list(map(int, input().split()))

res = snacks(N, stu)
print(res)