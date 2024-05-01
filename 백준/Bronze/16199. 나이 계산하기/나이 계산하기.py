birth = list(map(int, input().split()))
now = list(map(int, input().split()))
res = []
# age1 : 만 나이
# age2 : 세는 나이
# age3 : 연 나이
age1 = age2 = age3 = 0  

for i in range(len(birth)) :
    res.append(now[i] - birth[i])

if res[1] < 0 :
    age1 = res[0] - 1
elif res[1] == 0 :
    if res[2] < 0 :
        age1 = res[0] - 1
    else :
        age1 = res[0]
else :
    age1 = res[0]

age2 = res[0] + 1
age3 = res[0]
print(age1)
print(age2)
print(age3)