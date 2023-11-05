T = int(input())

for _ in range(T) :
    score, k = 0, 0
    lst = input().rstrip()
    for j in lst :
        if j == 'O' :
            k += 1
        else :
            k = 0

        score += k
    print(score)