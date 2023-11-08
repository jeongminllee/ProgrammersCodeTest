N, K = map(int, input().split())
lst = [int(input()) for _ in range(N)]
cnt = 0
while K != 0 :
    coin, K = divmod(K, lst[-1])
    lst.pop()
    cnt += coin

print(cnt)