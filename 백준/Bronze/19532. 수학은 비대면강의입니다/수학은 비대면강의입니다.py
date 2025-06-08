a, b, c, d, e, f = map(int, input().split())

calc_a1 = [d*a, d*b, d*c]
calc_a2 = [a*d, a*e, a*f]

calc_e1 = [e*a, e*b, e*c]
calc_e2 = [b*d, b*e, b*f]

res_a = [0, 0, 0]
res_e = [0, 0, 0]

ans = [0, 0]

for i in range(3) :
    res_a[i] = calc_a1[i] - calc_a2[i]
    res_e[i] = calc_e1[i] - calc_e2[i]

ans[0] = res_e[2] // res_e[0]
ans[1] = res_a[2] // res_a[1]

print(*ans)