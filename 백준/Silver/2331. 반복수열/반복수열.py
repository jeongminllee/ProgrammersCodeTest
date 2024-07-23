n, p = map(int, input().split())
arr = [n]
while True :
    num = arr[-1]
    lst = []
    for i in str(num) :
        lst.append(int(i) ** p)

    sm = sum(lst)
    if sm in arr :
        break
    arr.append(sm)

arr_ = arr[:arr.index(sm)]
print(len(arr_))