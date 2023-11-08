N = int(input())
positive = []
negative = []
answer = 0

for _ in range(N):
    num = int(input())
    if num > 1:
        positive.append(num)
    elif num == 1:
        answer += 1
    else :
        negative.append(num)

positive.sort(reverse=True) # 양수의 큰 수부터 정렬
negative.sort()             # 음수의 작은 수 부터 정렬

# 양수 리스트 더해주기
if len(positive) % 2 == 0:  # 양수가 짝수 개일 경우 두개 씩 곱해준다.
    for i in range(0, len(positive), 2) :
        answer += positive[i] * positive[i + 1]

else :
    for i in range(0, len(positive) - 1, 2) :
        answer += positive[i] * positive[i + 1]
    answer += positive[len(positive) - 1]   # 마지막 수는 더해준다

# 음수 더해주기
if len(negative) % 2 == 0:  # 음수가 짝수 개 일 경우 두 개씩 곱해준다.
    for i in range(0, len(negative), 2) :
        answer += negative[i] * negative[i + 1]

else :
    for i in range(0, len(negative) - 1, 2) :
        answer += negative[i] * negative[i + 1]
    answer += negative[len(negative) - 1]   # 마지막 수는 더해준다.

print(answer)
