def solution(n):
    answer = 0
    # 최대공약수
    for i in range(min(n, 6), 0, -1) : 
        if n % i ==0 and 6 % i ==0 :
            print(int(n/i))
            return int(n/i)
            break