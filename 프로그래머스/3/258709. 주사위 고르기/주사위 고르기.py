def get_wins_cnt(A, B) :
    '''
    :param A: A의 주사위
    :param B: B의 주사위
    :return: 모든 주사위 점수의 합에 따른 승리 횟수 반환(이분탐색)
    '''
    res = 0

    A.sort()
    B.sort()

    for a in A :
        # B 리스트에 대한 a의 lower bound(찾고자 하는 값 이상이 처음 나오는 위치)
        # = a가 몇 개의 경우의 수를 이기는지 개수
        start, end = 0, len(B) - 1

        while start <= end :
            mid = (start + end) // 2
            if a > B[mid] :
                start = mid + 1
            else :
                end = mid - 1

        res += end

    return res

def get_roll_result(dice, products, picks) :
    '''
    :param dice: 주사위 눈
    :param products: 주사위 n개를 굴리는 경우의 수(인덱스 조합)
    :param picks: 조합으로 얻은 주사위
    :return: 주사위 눈의 합
    주사위 pick에 따른 점수의 합의 모든 경우의 수 반환
    '''
    res = []
    for indice in products :
        tmp_sum = 0
        for idx, dice_idx in zip(indice, picks) :
            tmp_sum += dice[dice_idx][idx]
        res.append(tmp_sum)

    return res


def product(n) :
    '''
    :param n: 주사위 갯수
    :return: 주사위 n개를 굴리는 경우의 수(인덱스 조합) 반환
    '''
    res = []

    def recur(tmp):
        if len(tmp) == n:
            res.append(tmp)
            return

        for i in range(6):
            recur(tmp + [i])

    recur([])

    return res

def make_combinatinos(n, k) :
    '''
    :param n: 주사위 개수
    :param k: 조합 수
    :return: 조합

    주사위 n개 중 k개를 뽑는 조합 반환
    '''
    res = []

    def recur(tmp) :
        if len(tmp) == k :
            res.append(set(tmp))
            return

        for i in range(n) :
            if not tmp or i > tmp[-1] :
                recur(tmp + [i])

    recur([])

    return res

def solution(dice):
    n = len(dice)
    combinations = make_combinatinos(n, n // 2) # 주사위 조합
    products = product(n // 2)  # 주사위 면의 조합

    ans_cnt = 0
    answer = None   # 명시적 초기화

    for A_picks in combinations :
        B_picks = set(range(n)) - A_picks

        A_res = get_roll_result(dice, products, A_picks)    # A 주사위 결과
        B_res = get_roll_result(dice, products, B_picks)    # B 주사위 결과

        wins_cnt = get_wins_cnt(A_res, B_res)               # A 주사위가 이긴 횟수

        if ans_cnt < wins_cnt : # answer 업데이트
            ans_cnt = wins_cnt
            answer = sorted(list(map(lambda x:x+1, A_picks)))   # 인덱스가 1부터 시작함, 오름차순

    return answer