N = int(input())
lst = list(int(input()) for _ in range(N))

print(sum(lst) - (len(lst) - 1))