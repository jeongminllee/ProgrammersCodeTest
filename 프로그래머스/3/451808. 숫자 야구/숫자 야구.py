from typing import List

def permute(nums: List, end: int) :
    answer = []
    visited = [False for _ in range(len(nums))]
    permutations(0, end, nums, visited, [], 0, answer)
    return answer

def permutations(bgn: int, end: int, nums: List[str], visited: List[int], building: List[int], depth: int, answer):
    if depth == end :
        answer.append(building)
        return

    for idx in range(bgn, len(nums)) :
        if visited[idx] :
            continue

        visited[idx] = True
        permutations(0, end, nums, visited, building + [nums[idx]], depth+1, answer)
        visited[idx] = False

def solution(n, submit):
    # [1] 1~9에서 중복 없이 4개 고른 모든 후보 생성
    digits = '123456789'
    all_candidates = [''.join(p) for p in permute(digits, 4)]

    def score(secret: str, guess: str):
        strike = sum(a == b for a, b in zip(secret, guess))
        ball = sum(c in secret for c in guess) - strike
        return f"{strike}S {ball}B"

    for _ in range(n):
        guess = all_candidates[0]
        result = submit(int(guess))
        if result == '4S 0B':
            return int(guess)

        all_candidates = [x for x in all_candidates if score(x, guess) == result]

    return int(all_candidates[0])