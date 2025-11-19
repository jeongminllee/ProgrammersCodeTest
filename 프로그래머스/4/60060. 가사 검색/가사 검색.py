'''
from collections import defaultdict

class Trie :
    def __init__(self):
        # root는 dict
        # 각 노드에 '#' : 지나가는 단어 수를 저장
        self.root = {}

    def insert(self, word: str):
        curr = self.root
        # 루트를 지나가는 단어 수 +1
        curr['#'] = curr.get('#', 0) + 1

        for ch in word :
            if ch not in curr :
                curr[ch] = {}
            curr = curr[ch]
            # 이 노드를 지나가는 단어 수 +1
            curr['#'] = curr.get('#', 0) + 1
        curr["end_of_word"] = True

    def cnt_prefix(self, prefix: str):
        # prefix로 시작하는 단어가 몇 개인지 반환
        curr = self.root
        for ch in prefix :
            if ch not in curr :
                return 0
            curr = curr[ch]
        return curr.get('#', 0)

def solution(words, queries) :
    # 길이별 정방향 Trie, 역방향 Trie
    forword_tries = defaultdict(Trie)
    reverse_tries = defaultdict(Trie)

    # 단어 삽입
    for word in words :
        L = len(word)
        forword_tries[L].insert(word)       # 정방향
        reverse_tries[L].insert(word[::-1]) # 역방향

    answer = []
    cache = {}  # 같은 쿼리 여러 번 나올 수 있으니 캐싱

    for q in queries :
        if q in cache :
            answer.append(cache[q])
            continue

        L = len(q)

        # 쿼리 길이와 같은 단어가 아예 없는 경우
        # (defaultdict라 없어도 Trie는 생기지만, root에 '#'(카운트)가 없으면 0으로 처리됨)
        # 어차피 아래에서 처리되므로 생략 가능

        # [1] 앞부분의 글자, 뒷부분이 '?' 인 경우 : 접두사 검색
        if q[0] != '?' :
            # 처음 "?" 가 나오기 전까지 prefix
            prefix = q.split('?', 1)[0]
            cnt = forword_tries[L].cnt_prefix(prefix)

        # [2] 앞부분이 '?'이고, 뒷부분이 글자인 경우: 접미사 검색 -> 뒤집어서 prefix 처리
        else :
            # 왼쪽의 '?'들ㅇㄹ 제거하면 실제 접미사만 남음
            suffix = q.lstrip('?')

            # 전부 '?'인 경우: 해당 길이의 단어 개수 전체
            if suffix == "" :
                cnt = forword_tries[L].root.get('#', 0)
            else :
                # 단어를 뒤집어서 저장했으니, suffix를 뒤집어서 prefix로 검색
                rev_prefix = suffix[::-1]
                cnt = reverse_tries[L].cnt_prefix(rev_prefix)

        cache[q] = cnt
        answer.append(cnt)

    return answer
'''

def bisect_left(a, x) :
    left, right = 0, len(a)
    while left < right :
        mid = (left + right) // 2
        if a[mid] < x :
            left = mid + 1
        else :
            right = mid
    return left

def bisect_right(a, x) :
    left, right = 0, len(a)
    while left < right:
        mid = (left + right) // 2
        if a[mid] <= x:
            left = mid + 1
        else:
            right = mid
    return left

def cnt_in_range(words, left_value, right_value) :
    right_idx = bisect_right(words, right_value)
    left_idx = bisect_left(words, left_value)
    return right_idx - left_idx

def solution(words, queries) :
    answer = []

    max_len = 10000
    data = [[] for _ in range(max_len + 1)]
    reverse = [[] for _ in range(max_len + 1)]

    for word in words :
        L = len(word)
        data[L].append(word)
        reverse[L].append(word[::-1])

    for i in range(max_len + 1) :
        if data[i] :
            data[i].sort()
        if reverse[i] :
            reverse[i].sort()

    for query in queries :
        L = len(query)

        if not data[L] :
            answer.append(0)
            continue

        if query[0] != '?' :
            left_value = query.replace('?', 'a')
            right_value = query.replace('?', 'z')
            result = cnt_in_range(data[L], left_value, right_value)

        else :
            reversed_query = query[::-1]
            left_value = reversed_query.replace('?', 'a')
            right_value = reversed_query.replace('?', 'z')
            result = cnt_in_range(reverse[L], left_value, right_value)

        answer.append(result)

    return answer