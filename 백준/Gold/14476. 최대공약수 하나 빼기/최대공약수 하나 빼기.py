def my_gcd(a, b) :
    while b != 0 :
        a, b = b, a%b
    return a

def main() :
    '''
    N개의 정수 중에서 임의의 수 K를 뺐을 때,
    나머지 N-1개의 최대공약수가 가장 커지는 것을 찾는 프로그램을 작성하시오.
    이때, 최대공약수는 K의 약수가 되면 안 된다.

    :return : 가장 큰 최대공약수, 제거한 수를 출력
    '''
    N = int(input())
    arr = list(map(int, input().split()))


    # prefix GCD
    L = [0] * N
    L[0] = arr[0]

    for i in range(1, N) :
        L[i] = my_gcd(L[i-1], arr[i])

    # suffix GCD
    R = [0] * N
    R[N-1] = arr[N-1]
    for i in range(N-2, -1, -1) :
        R[i] = my_gcd(R[i+1], arr[i])

    best_g = 0
    best_k = -1

    for i in range(N) :
        if i == 0 :
            g = R[1]    # arr[1...N-1]의 GCD
        elif i == N-1 :
            g = L[N-2]  # arr[0...N-2]의 GCD
        else :
            g = my_gcd(L[i-1], R[i+1])  # arr[0...i-1]과 arr[i+1...N-1]의 GCD

        # g는 나머지 N-1의 GCD
        # 조건: g가 arr[i]의 약수가 아니어야 함.
        if arr[i] % g != 0 :
            if g > best_g :
                best_g = g
                best_k = arr[i]

    if best_g == 0 :
        print(-1)
    else :
        print(best_g, best_k)

if __name__ == "__main__" :
    main()