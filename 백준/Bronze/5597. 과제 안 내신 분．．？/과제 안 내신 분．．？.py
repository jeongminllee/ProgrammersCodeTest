X = [x for x in range(1, 31)]

for _ in range(28) :
    n = int(input())
    X.remove(n)
    
print(min(X))
print(max(X))

x = list(map(int, range(1, 31)))

for i in range(28) :
    x.remove(int(input()))
    
for j in x :
    print(j)
