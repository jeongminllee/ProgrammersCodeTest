# 칠하는 섹션을 max, min 의 차?
# while 문 쓰면 한방에 해결이 되는구나 => 왜 틀렸지?

# 횟수로 리턴
def solution(n, m, section):
    answer = 0
    cnt = 0
    while cnt < len(section) :
        s = section[cnt]
        e = s + m - 1
        while cnt < len(section) and section[cnt] <= e :
            cnt += 1
        answer += 1
    return answer