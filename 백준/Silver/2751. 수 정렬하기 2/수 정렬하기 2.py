N = int(input())
lst = []
for _ in range(N) :
    n = int(input())
    lst.append(n)

lst.sort()
print(*lst, sep='\n')