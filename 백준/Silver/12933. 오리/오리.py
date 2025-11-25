def main() :
    S = input().strip()
    quack = "quack"

    step = {}
    for i in range(len(quack)) :
        step[quack[i]] = i

    # 울음소리의 상태를 추적하는 배열
    cnts = [0] * 5
    ducks = 0
    max_duck = 0

    for ch in S :
        if ch not in step :
            print(-1)
            return

        idx = step[ch]

        if idx == 0 :   # 'q' 가 나왔을 때
            cnts[0] += 1
            ducks += 1
            max_duck = max(max_duck, ducks)
        else :
            if cnts[idx-1] > 0 :    # 이전 단계의 문자가 있는지 확인
                cnts[idx-1] -= 1
                cnts[idx] += 1
                if idx == 4 :   # 'k' 일 때, 하나의 울음이 끝났으므로 ducks 감소
                    ducks -= 1
            else :
                print(-1)
                return

    if ducks != 0 :
        print(-1)
    else :
        print(max_duck)

if __name__ == "__main__" :
    main()