def solution(number, limit, power):
    arr = []
    for i in range(1, number + 1) :
        num = 0
        for j in range(1, int(i ** 0.5) + 1) :
            if i % j == 0 :
                num += 1
                if j ** 2 != i :
                    num += 1
                    
            if num > limit :
                num = power
                break
        arr.append(num)
    return sum(arr)