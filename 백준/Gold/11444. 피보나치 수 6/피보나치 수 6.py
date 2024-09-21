from collections import defaultdict

def F(num) :
    if num <= 2 :
        return memo[num]
    # 중복 연산 막음 : 메모 활용
    elif memo[num] > 0 :
        return memo[num]
    # 해시값 존재 하지 않을 경우, 최소 한번은 연산해주어야 함.
    else :
        mid = num // 2
        if num % 2 == 0 :
            h0 = F(mid + 1)
            h1 = F(mid - 1)
            memo[num] = (h0 ** 2 - h1 ** 2) % 1_000_000_007
            return memo[num]
        else :
            h0 = F(mid + 1)
            h1 = F(mid)
            memo[num] = (h0 ** 2 + h1 ** 2) % 1_000_000_007
            return memo[num]

N = int(input())
memo = defaultdict(int)
memo[1], memo[2] = 1, 1
print(F(N))