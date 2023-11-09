from collections import deque

def solution(begin, target, words):
    visited = []
    q = deque([(begin, 0)])

    while q :
        cur_word, cur_cnt = q.popleft()

        if cur_word == target :     # 목표 단어를 찾은 경우
            return cur_cnt
        # 현재 단어를 거쳐갈 수 있는 다음 단어들을 찾아 큐에 추가
        for word in can_change(cur_word, set(words) - set(visited)) :
            q.append((word, cur_cnt + 1))
            visited.append(word)

    return 0

def can_change(cur_word, words) :
    c = []
    for word in words :
        diff = [True for x, y in zip(cur_word, word) if x != y]
        if len(diff) == 1 :     # 한 개의 알파벳만 다를 경우
            c.append(word)

    return c