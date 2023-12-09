def fib(n):
    arr1 = 1
    arr2 = 0
    now = 0

    if n <= 1:
        return n

    for i in range(2, n + 1):
        arr2 = now
        now = arr1
        arr1 = now + arr2

    return arr1

n = [0 for _ in range(491)]
n[1] = 1

while 1 :
    i = int(input())
    if i == -1 :
        break
    print(f"Hour {i}: {fib(i)} cow(s) affected")