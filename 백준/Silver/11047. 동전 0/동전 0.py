n, k = map(int, input().split())
coins = list(int(input()) for _ in range(n))
cnt = 0
while k != 0 :
    coin, k = divmod(k, coins[-1])
    coins.pop()
    cnt += coin

print(cnt)