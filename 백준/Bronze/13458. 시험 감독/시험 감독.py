N = int(input())
lst = list(map(int, input().split()))
B, C = map(int, input().split())

ans = N             # 총 감독관은 시험장의 개수 만큼
for n in lst :
    if n - B > 0 :  # 총 감독관이 감독한 인원 외의 인원을 부감독관에게 할당
        ans += (n - B + C - 1) // C
print(ans)