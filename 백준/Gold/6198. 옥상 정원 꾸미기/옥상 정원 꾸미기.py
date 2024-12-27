# 빌딩 갯수 입력받기
N = int(input())
arr = [int(input()) for _ in range(N)]

stack = []
res = []

for i in range(N - 1, -1, -1) :
    cnt = 0
    for j in range(len(stack)) :
        if stack[-1][0] < arr[i] :
            cnt += stack[-1][1] + 1
            stack.pop()
        elif stack[-1][0] >= arr[i] :
            stack.append([arr[i], cnt])
            break
    
    if len(stack) == 0 :
        stack.append([arr[i], cnt])
        
    res.append(cnt)

ans = 0
for num in res :
    ans += num

print(ans)