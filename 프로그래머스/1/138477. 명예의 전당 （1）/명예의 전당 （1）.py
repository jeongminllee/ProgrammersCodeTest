# 명예의 전당에 등록된 사람의 가장 낮은 점수를 return.
# 그냥 min으로 사용해서 해결
# 다른 방법은 뭐가 있을까

def solution(k, score):
    answer = []
    lst = []
    for i in range(len(score)) :
        lst.append(score.pop(0))
        lst.sort()
        answer.append(min(lst[:-(k + 1):-1]))
    return answer