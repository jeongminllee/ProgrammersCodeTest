def main() :
    # 항소의 초기 체력, 가지고 있는 먹이 개수
    n, m = map(int, input().split())

    print(len(bin(n)[2:]) + m)
    
    '''
    while n > 0 :
        m += 1
        n //= 2
    print(m)
    '''
T = int(input())
for _ in range(T) :
    main()