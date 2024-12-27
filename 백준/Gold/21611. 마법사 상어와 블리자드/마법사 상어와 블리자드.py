# T = int(input())
def main() :
    N, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    M = N // 2

    # [0] pos[] : 1차원 리스트에서 pos참조하여 달팽이 읽기/쓰기
    # 왼쪽 방향부터 반시계방향
    di = [0, 1, 0, -1]
    dj = [-1, 0, 1, 0]
    cnt_mx, cnt, flag = 1, 0, 0
    ci, cj, dr = M, M, 0        # 중앙 위치로 초기화, 방향(방향은 상관없음 -> 어차피 인접 비교)
    pos = []

    for t in range(N*N-1) :
        cnt += 1
        ci, cj = ci+di[dr], cj+dj[dr]
        pos.append((ci, cj))
        if cnt == cnt_mx :              # 2차원(달팽이) <-> 1차원 lst
            cnt = 0                     # 방향 변경
            dr = (dr + 1) % 4
            if flag == 0 :
                flag = 1
            else :
                flag = 0                # 두 번에 한 번씩 길이 증가
                cnt_mx += 1

    def bomb(lst) :
        # global ans    # main() 에 아닐때
        nonlocal ans    # main() 함수 안에서 실행할 때
        
        nlst = []       # 리턴에 사용
        lst.append(-1)  # 패딩
        i = 0
        while i < (len(lst)-1) :
            j = i + 1
            while lst[i] == lst[j] :
                j += 1
            if 4 <= (j - i) :   # 폭발
                ans += lst[i] * (j - i) # 구슬 번호 * 폭발 개수
            else :
                nlst += [lst[i]] * (j - i)

            i = j

        lst.pop()
        return nlst

    di = [0, -1, 1, 0, 0]
    dj = [0, 0, 0, -1, 1]
    ans = 0
    for _ in range(C) :                 # 명령의 개수만큼 d, s
        d, s = map(int, input().split())

        # [1] d방향으로 s만큼 뻗어가면서 arr을 0으로 변경 후 1차원 lst에 저장
        for mul in range(1, s+1) :
            arr[M+di[d]*mul][M+dj[d]*mul] = 0

        lst = []        # 0이 아닌 실제 구슬만 담기
        for (i, j) in pos :
            if arr[i][j] > 0 :
                lst.append(arr[i][j])

        # [2] 연속 4개 이상 폭발시키고 (더 이상 폭발하지 않을때 까지 반복)
        while True :
            tlst = bomb(lst)        # 4개 이상 폭발(점수 추가), 나머지 반환
            if len(tlst) == len(lst):   # 더이상 폭발하지 않음
                break
            lst = tlst

        # [3-1] 구슬을 개수 + 번호로 변환
        lst = []
        tlst.append(-1)         # 마지막 데이터 처리를 위해 패딩 추가 => 나중에 제거 필요
        i = 0
        while i < (len(tlst) - 1) :
            j = i + 1
            while tlst[i] == tlst[j] :  # 같은 동안 증가
                j += 1
            lst += [(j-i), tlst[i]] # 개수 + 번호를 추가
            i = j

        # [3-2] 1차원 -> 2차원 배열에 복사
        arr = [[0] * N for _ in range(N)]
        for i in range(0, min(len(lst), len(pos))) :
            arr[pos[i][0]][pos[i][1]] = lst[i]

    print(ans)

if __name__ == "__main__" :
    # for _ in range(T) :
    #     main()
    main()