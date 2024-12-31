# 1. 입력 및 초기화
N = int(input())
graph = [[0] * 58 for _ in range(58)]   # 58x58 2차원 배열 초기화(알파벳 대문자 A-Z기준, 26 + 여유 공간)
X = 0   # 총 관계 수 카운트

# 2. 초기 입력 관계
for _ in range(N) :
    left, right = input().split(' => ') # 관계 입력 받기
    if left == right :                  # 자기 자신으로 가는 관계는 무시
        continue
    P = ord(left) - 65      # 왼쪽 문자 ASCII 코드 기반 인덱스
    Q = ord(right) - 65     # 오른쪽 문자 ASCII 코드 기반 인덱스
    if graph[P][Q] == 0 :   # 새로운 관계라면
        graph[P][Q] = 1
        X += 1              # 관계 수 증가
        
# 3. 경로 추론 : 플로이드-워셜 알고리즘
for k in range(58) :        # 중간 정점
    for i in range(58) :    # 시작 정점
        for j in range(58): # 도착 정점
            if i != j and not graph[i][j] and graph[i][k] and graph[k][j] :
                graph[i][j] = 1
                X += 1

# 4. 결과 출력
print(X)
for i in range(58) :
    for j in range(58) :
        if i == j :
            continue
        if graph[i][j] :
            print(f'{chr(i + 65)} => {chr(j + 65)}')