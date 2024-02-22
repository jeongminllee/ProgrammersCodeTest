n = int(input())
arr = [[] for _ in range(201)]  # 제한 사항 : 1 <= age <= 200

for _ in range(n) :
    age, name = input().split()
    age = int(age)
    arr[age].append((age, name))

for i in range(201) :
    for a in arr[i] :
        print(a[0], a[1])