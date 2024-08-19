import sys
input = sys.stdin.readline

N, M = map(int, input().split())
keywords = {}
ans = 0

for _ in range(N) :
    keywords[input().rstrip()] = 1
    ans += 1

for _ in range(M) :
    post = list(input().rstrip().split(','))
    for i in post :
        if i in keywords.keys() :
            if keywords[i] == 1 :
                keywords[i] = 0
                ans -= 1
    print(ans)