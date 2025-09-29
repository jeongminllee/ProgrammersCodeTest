N, M = map(int, input().split())    # 사람의 수, 파티의 수
talk_true = list(map(int, input().split())) # 진실을 아는 사람의 수, [번호]
party_list = []
for _ in range(M) :
    st = list(map(int, input().split()))
    party_list.append(st[1:])

true_set = set()
if talk_true[0] != 0 :
    true_set.update(talk_true[1:])

for _ in range(M) :
    for party in party_list :
        party = set(party)
        if party & true_set :
            true_set = true_set|party

res = 0
for party in party_list :
    party = set(party)
    if set(party) & true_set :
        continue
    res += 1
print(res)