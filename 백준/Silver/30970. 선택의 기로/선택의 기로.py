N = int(input())
first = []  # 첫 번째 방법에 따라 정렬
second = [] # 두 번째 방법에 따라 정렬

for _ in range(N) :
    a, b = map(int, input().split())
    first.append((-a, b))   # 품질을 음수로 변환하여 정렬 시 높은 품질이 앞에 오도록 함
    second.append((b, -a))  # 가격은 그대로, 품질은 음수로 변환하여 정렬 시 낮은 가격이 앞에 오고, 같은 가격일 경우 높은 품질이 앞에 오도록 함

first.sort()
second.sort()

print(-first[0][0], first[0][1], -first[1][0], first[1][1])
print(-second[0][1], second[0][0], -second[1][1], second[1][0])