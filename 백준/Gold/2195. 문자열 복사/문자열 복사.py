S = input()
P = input()
idx_p = 0
res = 0

while idx_p < len(P) :
    max_val = tmp = idx_s = 0
    while idx_s < len(S) and idx_p + tmp < len(P) :
        if P[idx_p + tmp] == S[idx_s] :
            tmp += 1
            max_val = max(max_val, tmp)
        else :
            tmp = 0

        idx_s += 1
    idx_p += max_val
    res += 1
print(res)