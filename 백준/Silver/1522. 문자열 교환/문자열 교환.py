s = list(input())
n = len(s)
res = []
a_cnt = s.count('a')

for i in range(n) :
    # 원형 처리
    if n < i + a_cnt :
        tmp = s[i:] + s[:(i+a_cnt) % n]
    
    else :
        tmp = s[i:i+a_cnt]
    res.append(tmp.count('b'))
    # res.append(tmp)
# print(*res, sep='\n')
print(min(res))