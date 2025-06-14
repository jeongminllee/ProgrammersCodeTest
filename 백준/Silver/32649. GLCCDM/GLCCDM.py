from math import gcd
from itertools import combinations
import sys
import math

def lcm(a, b):
    return a * b // gcd(a, b)

def total_lcm(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = lcm(result, num)
        if result > 10**6:
            return -1
    return result

def solve(A, B, K):
    if B % A != 0:
        print(-1)
        return
    T = B // A

    # T의 약수 구하기
    divisors = []
    for i in range(1, int(T**0.5) + 1):
        if T % i == 0:
            divisors.append(i)
            if i != T // i:
                divisors.append(T // i)
    divisors.sort()

    # K개를 뽑아 조건을 만족하는지 확인
    for comb in combinations(divisors, K):
        if math.gcd(*comb) == 1 and total_lcm(comb) == T:
            result = [A * x for x in comb]
            print(" ".join(map(str, result)))
            return
    print(-1)

# 입력 처리
A, B, K = map(int, input().split())
solve(A, B, K)
