import sys
input = sys.stdin.readline

cale = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def sol_26148() :
    # 윤년의 조건
    # 4의 배수, not 100의 배수
    # 400의 배수
    N = int(input())
    days = int(input()) # 요일
    ans = 0

    if (N % 4 == 0 and N % 100 != 0) or (N % 400 == 0) :
        ans += 1

    ans += sum(cale) - 28 * 12

    print(ans)


sol_26148()