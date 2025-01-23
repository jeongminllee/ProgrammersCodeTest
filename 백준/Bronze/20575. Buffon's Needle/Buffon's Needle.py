def trunc(x) :
    if x >= 0 :
        return int(x)
    else :
        return -int(abs(x) + 1)
    
def main() :
    # the number of needles
    N = int(input())

    cnt = 0
    for _ in range(N) :
        # 바늘의 시작점과 끝점 좌표
        x1, y1, x2, y2 = map(float, input().split())

        # 버리기
        x1_trunc = trunc(x1)
        x2_trunc = trunc(x2)

        frac = abs(x1_trunc - x2_trunc)
        if frac > 0 :
            cnt += 1

    X = cnt / N
    pi = 2 / X

    print('{:.6f}'.format(pi))

    # pi = 2 / X => pi 를 구하는 ...
    # 실수를 구하는 문제
    # x의 수직선에 걸리는? 바늘의 개수를 찾는 그런 문제인 것 같다.
    # 그럼 y 는 필요가 없네?
    # x1 - x2 가 정수이기만 하면 이 문제는 풀리는거 아닌가?
    # 아 그게 아니라 그냥 x가 정수인 부분만 넘기는 바늘 갯수만 세면 되네
    # 그럼 그냥 1.999999 => 2.000001 도 x=2 에 걸쳐지는 거니까
    # 소수점 이하는 버리고 차이의 절대값이 0 보다 크기만 하면 된다.
    # 그냥 int 로 취하니까 오류가 난다.
    # 음수가 있어서? 그런걸까?
main()