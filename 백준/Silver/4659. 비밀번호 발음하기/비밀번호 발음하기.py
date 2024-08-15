aeiou = ('a', 'e', 'i', 'o', 'u')

while True :
    cmd = input()
    if cmd == 'end' :
        break

    x = y = cnt = 0
    for i in aeiou :
        if i in cmd :
            cnt += 1

    if cnt < 1 :
        print(f'<{cmd}> is not acceptable.')
        continue

    for i in range(len(cmd) - 2) :
        if cmd[i] in aeiou and cmd[i+1] in aeiou and cmd[i+2] in aeiou or \
                not(cmd[i] in aeiou) and not(cmd[i + 1] in aeiou) and not(cmd[i + 2] in aeiou) :
            x = 1

    if x == 1 :
        print(f'<{cmd}> is not acceptable.')
        continue

    for i in range(len(cmd) - 1) :
        if cmd[i] == cmd[i + 1] :
            if cmd[i] == 'e' or cmd[i] == 'o' :
                continue
            else :
                y = 1

    if y == 1 :
        print(f'<{cmd}> is not acceptable.')
        continue

    print(f'<{cmd}> is acceptable.')