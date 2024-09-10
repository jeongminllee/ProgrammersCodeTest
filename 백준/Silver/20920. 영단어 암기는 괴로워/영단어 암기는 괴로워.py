N, M = map(int, input().split())
words = {}  # Counter 할 딕셔너리 생성
lst = []    # 단어장
for _ in range(N) :
    S = input()
    if len(S) < M : # S의 길이가 M 미만이면
        continue

    if S not in words :
        words[S] = 1
    else :
        words[S] += 1

for word, val in words.items() :
    lst.append((word, val))

# 1. 등장 횟수가 많을수록 
# 2. 단어 길이가 길수록 
# 3. 알파벳 순으로
lst.sort(key=lambda x:(-x[1], -len(x[0]), x[0]))

for w in lst :
    print(w[0])