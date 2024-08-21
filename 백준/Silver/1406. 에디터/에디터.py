S1 = list(input().rstrip())
S2 = []
M = int(input())

for _ in range(M) :
    cmd = input()
    if cmd.startswith('P') :
        c, d = cmd.split()
        S1.append(d)

    else :
        if cmd == 'L' and S1 :
            S2.append(S1.pop())
        elif cmd == 'D' and S2 :
            S1.append(S2.pop())
        elif cmd == 'B' and S1 :
            S1.pop()

S1.extend(reversed(S2))
print(''.join(S1))