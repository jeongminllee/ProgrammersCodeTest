T = int(input())    # 테스트 케이스
for _ in range(T) :
    M = int(input())    # 입출 이벤트 개수
    curr = 0            # 현재 집 안에 있는 사람 수
    min_start = 0       # 처음에 있어야 했던 최소 인원
    
    for _ in range(M) :
        p1, p2 = map(int, input().split())  # 입장, 퇴장
        curr += p1  # 입장한 사람 더하기
        
        if curr >= p2 :
            curr -= p2 # 퇴장할 수 있는 만큼 퇴장
        else :
            # 퇴장 인원이 부족하면, 처음부터 그만큼 더 있어야 함
            min_start += (p2 - curr)
            curr = 0
            
    print(min_start)