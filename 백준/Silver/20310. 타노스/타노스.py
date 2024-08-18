S = list(input())

n = S.count('0')
m = S.count('1')

cnt_0 = 0
cnt_1 = 0

for i in S :
    if cnt_1 == m//2 :
        break
    if i == '1' :
        S.remove(i)
        cnt_1 += 1

S = S[::-1]
for i in S :
    if cnt_0 == n//2 :
        break
    if i == '0' :
        S.remove(i)
        cnt_0 += 1

for i in S[::-1] :
    print(i, end='')