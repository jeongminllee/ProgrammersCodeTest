ans, n = 0, 100
for i in range(100):
    print(f"? {i + 1} 1")
    s = input()
    if s == "ArrayIndexOutOfBoundsException":
        n = i
        break
    else:
        ans = max(ans, int(s))

for y in range(2, n + 1):
    for x in range(1, n + 1):
        print(f"? {x} {y}")
        ans = max(ans, int(input()))

print(f'! {ans}')