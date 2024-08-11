N = int(input())

cnt = 0
if N < 100 :
    cnt += N

else :
    for n in range(100, N + 1) :
        # 100자리 수 - 10의 자리 수 == 10의 자리수 - 1의 자리수
        if n//100 - n%100//10 == n%100//10 - n%10 :
            cnt += 1
    cnt += 99

print(cnt)