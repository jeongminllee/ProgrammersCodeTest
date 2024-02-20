def find_generator(n):
    for i in range(max(0, n - 54), n):
        if i + sum(map(int, str(i))) == n:
            return i
    return 0

n = int(input())
print(find_generator(n))