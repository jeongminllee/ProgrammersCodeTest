A = int(input())            # N의 진짜 약수의 개수
lst = list(map(int, input().split()))   # N의 진짜 약수

print(min(lst) * max(lst))