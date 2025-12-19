while True :
    try :
        meeting = list(map(int, input().split()))
        n = meeting[0]
        meeting = meeting[1:]
        nation = []
        for i in range(0, len(meeting), 2) :
            nation.append((meeting[i], meeting[i+1]))

        res = []
        for i in range(n) :
            x, y = nation[i]
            if i == n-1 :
                center_x = (nation[i][0] + nation[0][0]) / 2
                center_y = (nation[i][1] + nation[0][1]) / 2
            else :
                center_x = (nation[i][0] + nation[i+1][0]) / 2
                center_y = (nation[i][1] + nation[i+1][1]) / 2

            res.append(center_x)
            res.append(center_y)

        print(n, end=' ')
        for i in range(len(res)) :
            print(f"{res[i]:.6f}", end=' ')
        print()

    except :
        break