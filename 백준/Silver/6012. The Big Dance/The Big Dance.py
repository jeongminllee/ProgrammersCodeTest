res = 0

def processGroup(start, end) :
    global res
    cnt = end - start + 1

    # 기저 조건 1 : 한마리만 있으면
    if cnt == 1 :
        return

    elif cnt == 2:
        res += (start * end)    # 실제 번호가 start와 end일 경우, 두 숫자의 곱
        return
    
    # 분할 : 왼쪽 그룹과 오른쪽 그룹 결정
    # 왼쪽 그룹은 오른쪽 그룹보다 같거나 한 마리 더 많음
    if cnt % 2 == 0 :
        # 짝수 : 동일하게 분할
        mid = start + (cnt // 2) - 1
    else :
        # 홀수 : 왼쪽 그룹이 한 마리 더 많음
        mid = start + ((cnt + 1) // 2) - 1

    # 재귀 호출 : 두 그룹에 대해 처리
    processGroup(start, mid)   # 왼쪽 그룹 처리
    processGroup(mid + 1, end) # 오른쪽 그룹 처리


def sol_6012() :
    n = int(input())
    processGroup(1, n)

    print(res)
    
sol_6012()