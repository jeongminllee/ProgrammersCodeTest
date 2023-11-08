T = int(input())
lst = list(map(int, input().split()))
lst.sort()
answer = 0
for i in range(1, len(lst) + 1) :
    answer += lst[i - 1] * (len(lst) - i + 1)
print(answer)