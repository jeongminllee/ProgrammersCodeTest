a = list(map(int, input()))
b = list(map(int, input()))
lst = [0] * (len(a) + len(b))

for i in range(len(a) + len(b)) :
    if i % 2 == 0 :
        lst[i] = a[i // 2]
    else :
        lst[i] = b[i // 2]

while len(lst) != 2 :
    tmp = []
    for i in range(len(lst) - 1) :
        num = (lst[i] + lst[i + 1]) % 10
        tmp.append(num)
    lst = tmp

print(*lst, sep='')