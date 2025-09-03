def solution(D, N, diameters, pizza) :
    '''
    :param D: 오븐의 깊이
    :param N: 반죽의 개수
    :param diameters: 최상단부터 깊이에 따른 오븐의 지름
    :param pizza: 피자 반죽이 완성되는 순서
    :return: 마지막 피자 반죽의 위치
    '''
    oven = [diameters[0]]
    for i in range(1, D) :
        if diameters[i] > oven[i-1] :
            oven.append(oven[i-1])
        else :
            oven.append(diameters[i])

    pidx = 0
    i = D - 1
    while i >= 0 :
        if pizza[pidx] <= oven[i] :
            pidx += 1
            if pidx == N :
                break

        i -= 1

    if pidx < N :
        return 0
    else :
        return i + 1



if __name__ == '__main__' :
    D, N = map(int, input().split())
    diameters = list(map(int, input().split()))
    pizza = list(map(int, input().split()))
    print(solution(D, N, diameters, pizza))