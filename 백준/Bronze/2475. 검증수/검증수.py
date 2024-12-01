lst = list(map(int, input().split()))
res = [x ** 2 for x in lst]
ans = sum(res) % 10
print(ans)