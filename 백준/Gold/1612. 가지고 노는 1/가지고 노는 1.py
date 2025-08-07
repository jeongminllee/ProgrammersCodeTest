N = int(input())

if N == 1 :
    print(1)
elif N % 2 == 0 or N % 5 == 0 :
    print(-1)
else :
    x = 1
    time = 1
    while x%N != 0 :
        x = (x%N)*10 + 1
        time += 1
    print(time)