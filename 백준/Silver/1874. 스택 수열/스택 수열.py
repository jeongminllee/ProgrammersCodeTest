n = int(input())
cnt = 1
flag = True
stack = []
op = []

for i in range(n) :
    num = int(input())
    # num 이하 숫자까지 스택에 넣기
    while cnt <= num :
        stack.append(cnt)
        op.append('+')
        cnt += 1
    
    # num이랑 스택 맨 위 숫자가 동일하다면 제거
    if stack[-1] == num :
        stack.pop()
        op.append('-')
    
    # 스택 수열을 만들 수 없으므로 NO
    else :
        flag = False
        break
# 스택 수열을 만들 수 있은지 여부에 따라 출력
if flag == False :
    print("NO")
else :
    for i in op :
        print(i)