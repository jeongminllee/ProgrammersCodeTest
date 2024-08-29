S = input()
bomb = input()
stack = []

for i in range(len(S)) :
    stack.append(S[i])
    if ''.join(stack[-len(bomb):]) == bomb :
        for _ in range(len(bomb)) :
            stack.pop()

if stack :
    print(''.join(stack))
else :
    print("FRULA")