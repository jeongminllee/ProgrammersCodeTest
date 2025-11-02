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

    def score(secret: str, guess: str) :
        strike = sum(a == b for a, b in zip(secret, guess))
        ball = sum(c in secret for c in guess) - strike
        return f"{strike}S {ball}B"

    for _ in range(n) :
        guess = all_candidates[0]
        result = submit(int(guess))
        if result == '4S 0B' :
            return int(guess)
        
        all_candidates = [x for x in all_candidates if score(x, guess) == result]
        
    return int(all_candidates[0])