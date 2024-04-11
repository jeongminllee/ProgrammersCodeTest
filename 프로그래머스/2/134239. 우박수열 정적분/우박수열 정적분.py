# 그래프 생성
def make_graph(k) :
    graph = [k]
    while k != 1 :  # 콜라츠 수열
        if k % 2 == 0 :
            k //= 2
        else :
            k = k * 3 + 1
        graph.append(k)
    return graph

# 밑변은 항상 1이기 때문에 생각할 필요가 없음.
# 두 높이의 차를 반으로 나누어 삼각형 넓이를 구하고 두 지점 중 더 낮은 높이를 더해 밑변에 사각형 넓이를 구한다.
def cal_area(graph) :
    area = [0.0]    # 초기값 입력
    pre = graph[0]  
    for nxt in graph[1:] :  # graph[1] 부터
        area.append(min(pre, nxt) + abs(nxt - pre)/2)
        pre = nxt           # 값 이동
    return area

# 누적합은 직전까지의 합과 현재 더하려는 값을 더하여 순차적으로 구해주면 된다.
def cal_prefix_sum(area,n) :
    prefix_sum = [0] * n
    for i in range(1, n) :
        prefix_sum[i] = prefix_sum[i-1] + area[i]   # 누적합 계산
    return prefix_sum

def in_range(b, n) :
    return 0 <= b < n

def solution(k, ranges):
    answer = []
    graph = make_graph(k)                   # 콜라츠 수열 생성 
    area = cal_area(graph)                  # 각 구간의 면적 계산
    n = len(area)                           # 면적 리스트의 길이
    prefix_sum = cal_prefix_sum(area, n)    # 면적의 누적 합계 계산

    for a, b in ranges :
        b = n - 1 + b   # 6 - 1 - |b| 가 되는거 => 0, -1, -3, -3 => 5, 4, 2, 2
        if in_range(b, n) and a <= b :      # 유효한 범위 확인
            result = prefix_sum[b] - prefix_sum[a]  # 범위 내 면적 합계 
            answer.append(result)
        else :
            answer.append(-1.0)             # 유효하지 않은 범위에 대해 -1.0 반환
    return answer