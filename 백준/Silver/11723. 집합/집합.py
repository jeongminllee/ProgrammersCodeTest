import sys
input = sys.stdin.readline

M = int(input())
S = 0

for _ in range(M) :
    cmd = input().rstrip()
    if cmd == 'all' :
        S = (1 << 20) - 1

    elif cmd == 'empty' :
        S = 0

    else :
        c, num = cmd.split(' ')
        n = int(num) - 1
        if c == "add" :
            S |= (1 << n)
        elif c == "remove" :
            S &= ~(1 << n)
        elif c == "check" :
            print(1 if S & (1 << n) else 0)
        elif c == 'toggle' :
            S ^= (1 << n)