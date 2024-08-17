N = input().rstrip()
num = 0
idx = 0

while True :
    num += 1
    for s in str(num) :
        if N[idx] == s :
            idx += 1
            if idx >= len(N) :
                print(num)
                exit()