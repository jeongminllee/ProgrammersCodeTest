N = int(input())
positive = []
negative = []
zero = False
answer = 0

for _ in range(N):
    num = int(input())
    if num > 1:
        positive.append(num)
    elif num == 1 :
        answer += 1
    elif num < 0:
        negative.append(num)
    elif num == 0:
        zero = True

positive.sort(reverse=True)
negative.sort()

if len(positive) % 2 == 1:
    positive.append(1)

if len(negative) % 2 == 1:
    if zero:
        negative.append(0)
    else:
        answer += negative.pop()

for i in range(0, len(positive), 2):
    answer += positive[i] * positive[i+1]

for i in range(0, len(negative), 2):
    answer += negative[i] * negative[i+1]

print(answer)
