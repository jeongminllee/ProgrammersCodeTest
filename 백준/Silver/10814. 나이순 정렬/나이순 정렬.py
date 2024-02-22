n = int(input())
arr = []

for _ in range(n) :
    age, name = input().split()
    arr.append((age, name))

arr.sort(key=lambda x:int(x[0]))

for i in range(n) :
    print(arr[i][0], arr[i][1])