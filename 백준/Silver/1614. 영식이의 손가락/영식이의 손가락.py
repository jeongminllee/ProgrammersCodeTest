n = int(input())
m = int(input())
start = n - 1
lst = [(6, 2), (4, 4), (2, 6)]

if n == 1 or n == 5 :
    print(start + 8 * m)
elif n == 2 or n == 3 or n == 4 :
    for i in range(m) :
        start += lst[n-2][i%2]
    print(start)