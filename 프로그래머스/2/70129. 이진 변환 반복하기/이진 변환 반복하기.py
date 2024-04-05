def solution(s):
    cnt_rm = cnt_2 = 0
    
    while s != "1" :
        cnt_2 += 1
        cnt_rm += s.count("0")
        s = bin(s.count("1"))[2:]
    
    return [cnt_2, cnt_rm]