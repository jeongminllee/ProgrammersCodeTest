from collections import Counter

def solution(topping):
    split_cnt = 0
    topping_cnt = Counter(topping)
    half_topping_set = set()
    for t in topping :
        half_topping_set.add(t)
        topping_cnt[t] -= 1

        if topping_cnt[t] == 0 :
            topping_cnt.pop(t)

        if len(half_topping_set) == len(topping_cnt) :
            split_cnt += 1
    
    return split_cnt