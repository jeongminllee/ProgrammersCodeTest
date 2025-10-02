def num_to_bin(number) :
    bins = bin(number)[2:]
    n = 1
    
    while n < len(bins) :
        n = 2*n + 1
    return bins.zfill(n)

def trees(number, left, right) :
    if left >= right :
        return True
    
    mid = (left + right) // 2
    if number[mid] == '0' :
        if '1' in number[left:mid] or '1' in number[mid+1:right+1] :
            return False
    
    return trees(number, left, mid-1) and trees(number, mid+1, right)

def solution(numbers):
    answer = []
    for number in numbers :
        bits = num_to_bin(number)
        answer.append(int(trees(bits, 0, len(bits)-1)))
    return answer