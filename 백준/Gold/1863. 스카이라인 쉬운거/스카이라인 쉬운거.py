N = int(input())
ans = 0
stack = []
for _ in range(N) :
    a, b = map(int, input().split())
    if not stack :
        stack.append(b)
        continue
    while stack and b < stack[-1] :
        ans += 1
        stack.pop()

    if not stack or (stack and b != stack[-1]) :
        stack.append(b)

while stack :
    if stack[-1] > 0 :
        ans += 1
    stack.pop()
print(ans)