T = int(input())
arr = [0]

for _ in range(T) :
    x = int(input())
    arr.append(x)
g = [0, 0]
h = [0, arr[1]]


for i in range(2, T + 1) :
    g.append(h[i-1] + arr[i])
    h.append(max(g[i-2], h[i-2]) + arr[i])

print(max(g[T], h[T]))