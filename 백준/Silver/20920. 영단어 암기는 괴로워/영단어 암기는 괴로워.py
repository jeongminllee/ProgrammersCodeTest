N, M = map(int, input().split())
pad = {}

for i in range(N) :
    words = input()
    if len(words) < M :
        continue

    if words in pad :
        pad[words] += 1
    else :
        pad[words] = 1

arr = [i for i in pad.keys()]
arr.sort(key=lambda x:(-pad[x], -len(x), x))
print(*arr, sep='\n')