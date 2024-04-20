from collections import Counter
def solution(k, tangerine):
    counter = Counter(tangerine)
    sorted_counter = sorted(counter.values(), reverse = True)
    
    num = 0
    cnt = 0
    
    for count in sorted_counter :
        cnt += count
        num += 1

        if cnt >= k :
            break
            
    return num