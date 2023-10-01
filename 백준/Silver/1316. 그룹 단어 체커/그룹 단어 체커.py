N = int(input())
cnt = N

for i in range(N) :
    string = input()
    words = ''
    for s in string :
        if s not in words :
            words += s
        else :
            if words[-1] == s :
                words += s
            else :
                cnt -= 1
                break

print(cnt)
            