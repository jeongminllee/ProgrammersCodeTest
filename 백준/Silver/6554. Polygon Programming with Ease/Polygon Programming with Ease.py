while True :
    try :
        data = list(map(int, input().split()))
        n = data[0]
        meetings = []

        for i in range(1, len(data), 2) :
            meetings.append((data[i], data[i+1]))

        f0_x = f0_y = 0

        for i in range(n) :
            sign = 1 if i % 2 == 0 else -1
            f0_x += sign * meetings[i][0]
            f0_y += sign * meetings[i][1]

        offices = [(f0_x, f0_y)]

        for i in range(n-1) :
            f_nxt_x = 2 * meetings[i][0] - offices[-1][0]
            f_nxt_y = 2 * meetings[i][1] - offices[-1][1]
            offices.append((f_nxt_x, f_nxt_y))

        print(n, end=' ')
        for fx, fy in offices :
            print(f"{fx:.6f} {fy:.6f}", end=' ')
        print()


    except :
        break