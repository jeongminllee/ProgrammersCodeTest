import sys
from collections import deque

def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append([begin, 0])    # [단어, 깊이]
    v = [0] * (len(words))  # 방문 노드 여부 확인 리스트

    while q :
        print(q)
        word, cnt = q.popleft()
        if word == target :
            answer = cnt
            break
        for i in range(len(words)):
            temp_cnt = 0
            if not v[i] :   # 만약 확인 안 한 단어라면
                # 그 단어가 words 속 단어와 다를 때 한 자씩 비교해서 더하기
                for j in range(len(word)) :
                    if word[j] != words[i][j] :
                        temp_cnt += 1

                if temp_cnt == 1 :
                    q.append([words[i], cnt + 1])
                    v[i] = 1

    return answer