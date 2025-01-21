# 범위 설정
arr = []
for i in range(ord('a'), ord('z') + 1) :
    for j in range(ord('0'), ord('9') + 1) :
        arr.append(i ^ j)

N = int(input())
message = input().split()

res = ''
for m in message :
    # 16진수 문자열을 10진수로 변환
    dec = int(m, 16)
    # 64 <= dec <= 95 범위에 있으면 영소문자나 특수문자일 가능성이 있음
    res += '-' if min(arr) <= dec <= max(arr) else '.'

print(res)