# 접시 수, 초밥 가짓수, 연속해서 먹는 접시 수, 쿠폰 번호
N, d, k, c = map(int, input().split())

sushi = [int(input()) for _ in range(N)]
ans = 0
for i in range(N) :
    if i + k > N :
        res = len(set(sushi[i:N] + sushi[:(i+k)%N] + [c]))
    else :
        res = len(set(sushi[i:i+k] + [c]))

    ans = max(ans, res)

print(ans)