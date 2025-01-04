N = int(input())
lst = list(map(int, input().split()))
lst.sort()
# A : N의 진짜 약수가 되려면, 2 <= A <= 10 ** 6
# 2 4 를 약수로 둔 자연수의 경우, 4와 8이 해당 될것인데, 4가 되려면 1이 포함되어야 한다.
# 전제 조건에 위반하기 때문에 8이 정답이 될 것이다.

print(lst[0] * lst[-1])