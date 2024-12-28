import sys
input = sys.stdin.readline

S = input()
q = int(input())

prefix_sum_dict = {}

for _ in range(q) :
    a, l, r = input().split()
    l, r = int(l), int(r)

    if prefix_sum_dict.get(a) is None :
        prefix_sum = [0]
        sm = 0
        for ch in S :
            if ch == a :
                sm += 1
            prefix_sum.append(sm)
        prefix_sum_dict[a] = prefix_sum
    else :
        prefix_sum = prefix_sum_dict[a]
        
    print(prefix_sum[r+1] - prefix_sum[l])