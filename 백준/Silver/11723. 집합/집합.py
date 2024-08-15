import sys
input = sys.stdin.readline

M = int(input())
S = set()

for _ in range(M) :
    cmd = input().rstrip()
    if cmd == 'all' :
        S = set(i for i in range(1, 21))

    elif cmd == 'empty' :
        S.clear()

    else :
        c, num = cmd.split(' ')
        if c == "add" :
            S.add(int(num))
        elif c == "remove" :
            if int(num) not in S :
                continue
            else :
                S.remove(int(num))
        elif c == "check" :
            if int(num) in S :
                print('1')
            else :
                print('0')
        elif c == 'toggle' :
            if int(num) not in S :
                S.add(int(num))
            else :
                S.remove(int(num))