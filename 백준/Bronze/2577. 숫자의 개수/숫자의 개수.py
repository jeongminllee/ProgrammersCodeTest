A = int(input())
B = int(input())
C = int(input())

n = A * B * C
n_lst = list(str(n))
# print(n_lst)

cnt_lst = [0] * 10
# print(cnt_lst)

for i in range(10) :
    for n in n_lst :
        if i == int(n) :
            cnt_lst[i] += 1
            # print(cnt_lst)

for cnt in cnt_lst :
    print(cnt)