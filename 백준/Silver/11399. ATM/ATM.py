n = int(input())
lst = list(map(int, input().split()))
ans = [0] * n
lst.sort()

for i in range(n) :
    ans[i] = sum(lst[:i + 1])
print(sum(ans))