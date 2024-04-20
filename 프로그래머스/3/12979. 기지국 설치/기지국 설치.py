def solution(n, stations, w):
    answer = 0
    loc = 1 # 현재 탐색하는 아파트 위치
    i = 0   # 설치된 기지국의 인덱스
    
    while loc <= n :
        # 기지국이 설치된 위치에 도달한 경우
        if i < len(stations) and loc >= stations[i] - w :
            loc = stations[i] + w + 1
            i += 1
        # 기지국이 설치되지 않은 위치인 경우
        else :
            answer += 1
            loc += 2 * w + 1    # 기지국을 설치하고 해당 범위를 넘어감
    return answer