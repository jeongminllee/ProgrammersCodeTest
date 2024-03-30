def main():
    # 십의 자리 숫자에 따른 일의 자리 소수를 저장하는 딕셔너리 초기화
    prime_dict = dict()

    # 11부터 97까지 소수 판별 후, 해당하는 십의 자리에 일의 자리 숫자 저장
    for n in range(1, 10):
        prime_dict[str(n)] = []

    for i in range(11, 98):
        PRIME = True

        for t in range(2, 10):
            if i % t == 0:
                PRIME = False
                break

        if PRIME:
            prime_dict[str(i // 10)].append(str(i % 10))

    # 입력 받기
    A, B, N = input().split()
    N = int(N)

    # 조건 확인 : A의 자리와 B의 십의 자리가 소수의 조건을 만족하는지 확인
    if A[1] in prime_dict[A[0]] and B[1] in prime_dict[B[0]] and (B[0] in ['1', '3', '7', '9']):
        pass    # 조건을 만족하면 계속 진행
    else:
        print(-1)
        return 0

    # A의 일의 자리가 9인 경우와 그렇지 않은 경우를 나누어 소수소수 발생
    if A[1] == '9':
        # A의 일의 자리가 9인 경우, 7과 1을 적절히 사용하여 소수소수 생성
        print(A + '7' + '1' * (N - 5) + B)
    else:
        # A의 일의 자리가 9가 아닌 경우, 1만을 사용하여 소수소수 생성
        print(A + '1' * (N - 4) + B)

main()