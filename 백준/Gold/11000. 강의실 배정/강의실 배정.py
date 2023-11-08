import sys
input = sys.stdin.readline

N = int(input())

start, end = [], []
for _ in range(N) :
    a, b = map(int, input().split())
    start.append(a)
    end.append(b)

start.sort()
end.sort()

e = 0

for s in start :
    if end[e] <= s :
        e += 1
        N -= 1

print(N)