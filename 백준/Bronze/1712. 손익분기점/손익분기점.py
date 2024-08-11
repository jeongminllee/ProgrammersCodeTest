# A : 고정비용
# B : 변동비용
# C : 가격

def BEP(A, B, C) :
    if B >= C :
        return -1

    bp = C - B
    ans = (A // bp) + 1
    return ans

A, B, C = map(int, input().split())
print(BEP(A, B, C))