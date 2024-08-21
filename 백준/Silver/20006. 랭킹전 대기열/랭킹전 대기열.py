# 플레이어 수 P, 방의 정원 M 입력
P, M = map(int, input().split())
# 플레이어 입력(딕셔너리)
players = {}
# 방 생성(리스트)
rooms = []
# 플레이어 정보 기록
for _ in range(P) :
    L, N = input().split()
    players[N] = int(L)

# 각 플레이어 정보 불러오기
for name, level in players.items() :
    # 아직 방 없음
    flag = False
    
    for i in range(len(rooms)) :
        if len(rooms[i][1]) == M :
            continue
        
        # 제한 레벨 안에 들면
        if rooms[i][0] - 10 <= level <= rooms[i][0] + 10 :
            # 방이 있는거니까
            flag = True
            rooms[i][1].append(name)    # 생성된 방에 아이디 입력
            break

    # 방이 없으니까 생성
    if not flag :
        rooms.append([level, [name]])   # 제한 레벨, 아이디 입력

# 모든 플레이어 배정 끝났다면
# 방 안의 정보를 불러와서
for i in rooms :
    # 플레이어가 정원만큼 들어왔다면
    if len(i[1]) == M :
        print("Started!")
    # 플레이어 정원이 덜 찼다면
    else :
        print("Waiting!")

    # 방 안의 정보를 하나씩 불러온다(레벨, 아이디)
    for j in sorted(i[1]) :
        print(players[j], j)