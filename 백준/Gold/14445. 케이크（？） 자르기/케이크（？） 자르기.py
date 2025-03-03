def sol_14445() :
    # 10**18 이하의 자연수 N
    N = int(input())
    print(0 if N <= 1 else (N + 1) // 2)
    
sol_14445()