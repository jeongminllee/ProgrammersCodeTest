p, m = map(int, input().split())
users = []
for _ in range(p) :
    l, n = input().split()
    l = int(l)
    users.append([l, n])

rooms = []
for lv, uid in users :
    flag = False
    for i in range(len(rooms)) :
        if len(rooms[i][1]) == m :
            continue

        # 들어갈 수 있는 방이 있으면 입장
        if rooms[i][0] - 10 <= lv <= rooms[i][0] + 10 :
            flag = True
            rooms[i][1].append([lv, uid])
            break

    if not flag :
        rooms.append([lv, [[lv, uid]]])

# 방이 생성된 시간 순서로 출력
for i in range(len(rooms)) :
    if len(rooms[i][1]) == m :
        print("Started!")
        tmp = sorted(rooms[i][1], key=lambda x:x[1])
        for j in range(m) :
            print(*tmp[j])

    else :
        print("Waiting!")
        tmp = sorted(rooms[i][1], key=lambda x:x[1])
        for j in range(len(tmp)) :
            print(*tmp[j])