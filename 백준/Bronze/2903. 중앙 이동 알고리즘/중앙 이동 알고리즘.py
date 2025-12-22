N = int(input())
start = 2

for i in range(N) :
    start += 2 ** i
    
res = start ** 2
print(res)