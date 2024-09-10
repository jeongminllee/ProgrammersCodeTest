N, M = map(int, input().split())
words = {}
lst = []
for _ in range(N) :
    S = input()
    if len(S) < M :
        continue

    if S not in words :
        words[S] = 1
    else :
        words[S] += 1

for word, val in words.items() :
    lst.append((word, val))

lst.sort(key=lambda x:(-x[1], -len(x[0]), x[0]))

for w in lst :
    print(w[0])