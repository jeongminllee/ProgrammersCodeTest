S = input().upper()
char_count = {}

# Counter(S)
for char in S :
    char_count[char] = char_count.get(char, 0) + 1

# 가장 많이 나온 문자의 개수 찾기
max_count = max(char_count.values())

# 가장 많이 나온 문자들 찾기
most_common = [char for char, cnt in char_count.items() if cnt == max_count]

# 결과 출력
if len(most_common) > 1 :
    print("?")
else :
    print(most_common[0])
    
'''
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
    '''