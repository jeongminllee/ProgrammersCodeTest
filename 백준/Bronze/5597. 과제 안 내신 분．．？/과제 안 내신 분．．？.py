X = [x for x in range(1, 31)]

for _ in range(28) :
    n = int(input())
    X.remove(n)
    
print(min(X))
print(max(X))