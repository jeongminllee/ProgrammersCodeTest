n = int(input())
lst = list()
for i in range(n) :
    nums = 0
    for j in str(i) :
        nums += int(j)
    if nums + i == n :
        lst.append(i)

if len(lst) == 0 :
    print(0)
else :
    print(min(lst))