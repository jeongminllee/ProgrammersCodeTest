N = int(input())

scores = list(map(int, input().split()))

max_score = max(scores)

new_score = [(n / max_score) for n in scores]
new_mean = sum(new_score) / N * 100
print(new_mean)