N = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)
lst = [0] * N
answer = 0
for i in range(len(arr)) :
    lst[i] = sum(arr[:i + 1])
print(sum(lst))