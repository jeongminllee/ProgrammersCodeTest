d1 = int(input())
d2 = int(input())

pi = 3.141592
# A, B 랑은 같은 반원이니까 두 값의 합은 원이라 보면 됨
# 그럼 원둘레는 2*pi*d2 이고
# C의 둘레는 2 * (d1 + 2 * d2) => 운동장 둘레니까 d2는 빼야되는구나
circle = 2 * pi * d2
rectangle = 2 * d1

print(f"{circle + rectangle:.6f}")