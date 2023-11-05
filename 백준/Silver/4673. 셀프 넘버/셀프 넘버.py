def self_num(N) :
    num = list(str(N))
    ans = N
    for i in range(len(num)) :
        ans += int(num[i])

    return ans

lst = list(range(1, 10001))
for N in range(1, 10001) :
    if self_num(N) in lst :
        lst.remove(self_num(N))

for i in range(len(lst)) :
    print(lst[i])