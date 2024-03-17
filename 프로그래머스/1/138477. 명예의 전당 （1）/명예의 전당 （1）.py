# 명예의 전당에 등록된 사람의 가장 낮은 점수를 return.
# 힙을 써서 가장 낮은 애들을 pop 하는걸로
import heapq

def solution(k, score):
    answer = []
    lst = []
    for i in range(len(score)) :
        lst.append(score.pop(0))
        lst.sort()
        answer.append(min(lst[:-(k + 1):-1]))
    return answer