def robot_vacuum(N, M, start_r, start_c, start_d, room):
    # 방향: 북, 동, 남, 서 (0, 1, 2, 3)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    current_r, current_c, current_d = start_r, start_c, start_d
    cleaned_count = 0
    
    # 청소 상태를 저장하는 배열
    cleaned = [[False] * M for _ in range(N)]
    
    while True:
        # 현재 칸이 청소되지 않은 경우, 청소
        if not cleaned[current_r][current_c]:
            cleaned[current_r][current_c] = True
            cleaned_count += 1
        
        # 청소되지 않은 빈 칸이 있는지 확인
        found_empty = False
        
        for _ in range(4):
            # 방향을 반시계로 90도 회전
            current_d = (current_d + 3) % 4  # 왼쪽 회전
            new_r = current_r + directions[current_d][0]
            new_c = current_c + directions[current_d][1]
            
            # 새로운 위치가 청소되지 않은 빈 칸인지 확인
            if 0 <= new_r < N and 0 <= new_c < M and room[new_r][new_c] == 0 and not cleaned[new_r][new_c]:
                current_r, current_c = new_r, new_c  # 이동
                found_empty = True
                break
        
        # 청소되지 않은 빈 칸이 없는 경우
        if not found_empty:
            # 후진할 수 있는지 확인
            back_r = current_r - directions[current_d][0]
            back_c = current_c - directions[current_d][1]
            if room[back_r][back_c] == 1:  # 벽인 경우
                break  # 작동을 멈춤
            else:
                current_r, current_c = back_r, back_c  # 후진

    return cleaned_count

# 입력 받기
N, M = map(int, input().split())
start_r, start_c, start_d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

# 결과 출력
result = robot_vacuum(N, M, start_r, start_c, start_d, room)
print(result)
