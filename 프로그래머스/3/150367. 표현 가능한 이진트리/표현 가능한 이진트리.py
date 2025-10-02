def solution(numbers):
    def valid(s, left, right) :
        if left >= right :
            return True
        
        mid = (left + right) // 2
        if s[mid] == '0' :
            if '1' in s[left:mid] or '1' in s[mid+1:right+1] :
                return False
        
        return valid(s, left, mid-1) and valid(s, mid+1, right)
    
    answer = []
    for num in numbers :
        s = bin(num)[2:]
        L = 1
        while L < len(s) :
            L = 2*L + 1
        s = s.zfill(L)
        
        answer.append(int(valid(s, 0, len(s)-1)))
    
    return answer
