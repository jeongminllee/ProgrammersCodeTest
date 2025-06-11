# DNA 수, 문자 길이
N, M = map(int, input().split())

DNA = [list(input()) for _ in range(N)]

dnas = ['A', 'T', 'G', 'C']
dnas.sort()

res = ''
cnt = 0

for i in range(M) :
    cnt_dna = [0, 0, 0, 0]
    for j in range(N) :
        if DNA[j][i] == dnas[0] :
            cnt_dna[0] += 1
        elif DNA[j][i] == dnas[1] :
            cnt_dna[1] += 1
        elif DNA[j][i] == dnas[2] :
            cnt_dna[2] += 1
        else :
            cnt_dna[3] += 1

    res += dnas[cnt_dna.index(max(cnt_dna))]
    cnt += N - max(cnt_dna)
    
print(res)
print(cnt)