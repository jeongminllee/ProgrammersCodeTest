from collections import defaultdict

def permutations(chars: str, k: int):
    used = [0] * len(chars)
    res = []
    tmp = []

    def backtrack():
        if len(tmp) == k:
            res.append(tmp[:])
            return

        for i, ch in enumerate(chars) :
            if not used[i] :
                used[i] = True
                tmp.append(ch)
                backtrack()
                tmp.pop()
                used[i] = False

    backtrack()
    return res

def solution(n, submit):
    # [1] 1~9에서 중복 없이 4개 고른 모든 후보 생성
    digits = '123456789'
    all_candidates = [''.join(p) for p in permutations(digits, 4)]

    def score(a: str, b: str) -> tuple:
        s = sum(1 for i in range(4) if a[i] == b[i])
        # 공통 숫자 수 - 스트라이크 = 볼
        bcnt = sum(1 for ch in a if ch in b) - s
        return (s, bcnt)

    # 후보 집합을 유지하며 점점 좁혀가기
    candidates = all_candidates[:]
    used = set()

    # 시작 추측: 보통 정보량이 좋은 균형 잡힌 수 (예: 1357)
    # 후보 안에 반드시 존재하므로 그대로 사용
    current = '1357' if '1357' in candidates else candidates[0]

    for _ in range(n):
        used.add(current)
        xs_yb = submit(int(current))
        xs, yb = map(int, xs_yb.replace('S', '').replace('B', '').split())

        # 맞췄으면 끝
        if xs == 4:
            return int(current)

        # 단서와 일치한 후보만 남기기
        candidates = [c for c in candidates if score(c, current) == (xs, yb)]

        # 후보가 1개면 그게 정답
        if len(candidates) == 1:
            return int(candidates[0])

        # 후보가 없을 시 -> 예외처리
        if not candidates:
            return int(current)

        # 다음 추측 (휴리스틱)
        best_guess = None
        best_worst = 10 ** 9
        best_in_candidates = -1

        pool = candidates if len(candidates) <= 100 else candidates[:50]
        for g in pool:
            buckets = defaultdict(int)
            for c in candidates:
                buckets[score(c, g)] += 1
            worst = max(buckets.values())

            in_cand = 1
            if worst < best_worst or (worst == best_worst and in_cand > best_in_candidates):
                best_worst = worst
                best_in_candidates = in_cand
                best_guess = g

        # 실패했다면
        if best_guess is None:
            for c in candidates:
                if c not in used:
                    best_guess = c
                    break

            if best_guess is None:
                best_guess = candidates[0]

        current = best_guess

    return int(candidates[0] if candidates else current)