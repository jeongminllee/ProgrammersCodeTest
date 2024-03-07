def solution(numbers):
    answer = []
    n = len(numbers)
    for i in range(n - 1) :
        for j in range(i + 1, n) :
            a, b = numbers[i], numbers[j]
            if (a + b) in answer :
                continue
            answer.append(a + b)
            
    answer.sort()
            
    return answer