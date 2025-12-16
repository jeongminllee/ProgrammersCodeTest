# 티셔츠 한 장, 펜 한 자루
# 티셔츠 사이즈 : S, M, L, XL, XXL, XXXL, 같은 사이즈를 T장 묶음으로만 주문 가능
# 펜: 한 종류로, P자루씩 묶음으로 주문하거나 한 자루씩 주문 가능
# 티셔츠 : 남아도 됨, 부족하면 안됨. 신청한 사이즈대로 나누어 줘야함.
# 펜 : 참가자 수만큼 딱 준비되어 있어야 함.

N = int(input())
t_shirt = list(map(int, input().split()))
t_size, p_size = map(int, input().split())

# 정답
# 티셔츠를 T장씩 최소 몇 묶음 주문해야하는지 출력
# 펜 P자루씩 최대 몇 묶음 주문해야 하는지와 그 때 한 자루씩 몇 개 주문하는지
t_res, p_res = 0, 0
for t in t_shirt :
    if t // t_size :
        t_res += t // t_size
        if t % t_size :
            t_res += 1
    else :
        if t % t_size:
            t_res += 1

p_res = (N // p_size)

print(t_res)
print(p_res, N%p_size)