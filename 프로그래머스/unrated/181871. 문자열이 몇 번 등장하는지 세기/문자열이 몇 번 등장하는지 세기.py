def solution(myString, pat):
    start = 0
    count = 0
    
    while True :
        idx = myString.find(pat, start)
        if idx == -1 :
            break
        count += 1
        start = idx + 1
            
    
    return count