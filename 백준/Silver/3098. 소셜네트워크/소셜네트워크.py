import sys
input = sys.stdin.readline

def sol_3098() :
    N, M = map(int, input().split())
    friends = [set() for _ in range(N + 1)]

    # 초기 친구 관계 설정
    for _ in range(M) :
        A, B = map(int, input().split())
        friends[A].add(B)
        friends[B].add(A)

    days = 0
    daily_new_friends = []

    while True :
        new_count = 0
        for i in range(1, N + 1) :
            new_count += len(friends[i])

        if new_count == N * (N - 1) :
            break

        new_friend = set()

        # 각 사람에 대해 친구의 친구를 탐색
        for person in range(1, N + 1) :
            for friend in friends[person] : # 현재 친구 목록
                for f_of_f in friends[friend] : # 친구의 친구 목록
                    if f_of_f != person and f_of_f not in friends[person] : # 새로운 친구라면 추가
                        if person <= f_of_f :
                            new_friend.add((person, f_of_f))
                        else :
                            new_friend.add((f_of_f, person))

        for a, b in new_friend :
            friends[a].add(b)
            friends[b].add(a)

        days += 1
        daily_new_friends.append(len(new_friend))    # 친구 관계는 양방향이므로 // 2

    # 결과 출력
    print(days)
    for cnt in daily_new_friends :
        print(cnt)
        
sol_3098()