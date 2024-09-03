'''
1 1 1
2 2 ~ 7 6
3 8 ~ 19    12
4 20 ~ 37   18
5 38 ~ 61   24
6 62 ~ ...
N <= 1e9 이기 때문에 
O(N)
'''
N = int(input())
target = i = 1

while target < N :
    target += 6 * i
    i += 1

print(i)