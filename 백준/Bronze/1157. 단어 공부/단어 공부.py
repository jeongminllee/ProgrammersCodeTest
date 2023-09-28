S = input().upper()

unique_S = list(set(S))

cnt_list = []

for i in unique_S :
    cnt = S.count(i)
    cnt_list.append(cnt)
    
if cnt_list.count(max(cnt_list)) > 1 :
    print('?')
    
else :
    max_index = cnt_list.index(max(cnt_list))
    print(unique_S[max_index])