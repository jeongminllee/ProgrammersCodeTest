def solution(n, m):
    num1 = 0
    for i in range(1, n + 1) :
        if n % i == 0 and m % i == 0 :
            num1 = i
    num2 = (n * m) // num1
    
    return [num1, num2]