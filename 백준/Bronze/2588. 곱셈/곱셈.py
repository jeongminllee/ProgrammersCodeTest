a = int(input())
b = input()

ans1 = a * int(b[2])
ans2 = a * int(b[1])
ans3 = a * int(b[0])

ans = a * int(b)

print(ans1, ans2, ans3, ans, sep = '\n')