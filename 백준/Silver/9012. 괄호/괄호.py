T = int(input())

for _ in range(T) :
    ans = 0
    lst = input()

    for i in lst :
        if i == '(' :
            ans += 1
        elif i == ')' :
            if ans > 0 :
                ans -= 1
            else :
                print("NO")
                break
    else :
        if ans == 0 :
            print("YES")
        else :
            print("NO")
            
# T = int(input())
# 
# for t in range(T) :
#     stack = []
#     a = input()
#     for j in a :
#         if j == '(' :
#             stack.append(j)
#         elif j == ')' :
#             if stack :
#                 stack.pop()
#             else :
#                 print("NO")
#                 break
#     else :
#         if not stack :
#             print("YES")
#         else :
#             print("NO")