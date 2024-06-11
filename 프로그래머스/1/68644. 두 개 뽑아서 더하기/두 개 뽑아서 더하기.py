def solution(numbers) :
    lst = []
    for i in range(len(numbers)-1) :
        for j in range(i+1, len(numbers)) :
            lst.append(numbers[i] + numbers[j])
    lst = list(set(lst))
    return sorted(lst)