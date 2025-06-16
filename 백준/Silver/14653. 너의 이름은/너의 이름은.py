# 사람 수, 메시지 수, 정보를 알고 싶은 메시지 번호
N, K, Q = map(int, input().split())
reader = [{'A'} for _ in range(K)]
notReadCnt = []

for i in range(K) :
    notRead, sender = input().split()
    notReadCnt.append(int(notRead))

    if sender != 'A' :
        for j in range(i) :
            reader[j].add(sender)

    if i > 0 and notReadCnt[i] == notReadCnt[i-1] :
        reader[i] = reader[i-1]

    reader[i].add(sender)

if notReadCnt[Q-1] == 0 :
    print(-1)
else :
    for i in range(N) :
        if chr(ord('A') + i) not in reader[Q-1] :
            print(' '.join(chr(ord('A') + i)), end=' ')