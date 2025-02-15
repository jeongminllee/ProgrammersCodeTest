import sys
input = sys.stdin.readline

def sol_32249() :
    N, M = map(int, input().split())
    Alice = [list(input().rstrip()) for _ in range(N)]
    Bob = [list(input().rstrip()) for _ in range(N)]

    AcntB = sum(i == 'B' for j in Alice for i in j)
    sB = {i for i in range(M) if Alice[-1][i]=='B'}

    BcntA = sum(i == 'A' for j in Bob for i in j)
    sA = {i for i in range(M) if Bob[-1][i] == 'A'}

    def check_cond() :
        Aturn = 1 + (AcntB - bool(sB)) * 2
        Bturn = (1 + BcntA-bool(sA)) * 2
        print(['Bob', 'Alice'][Aturn < Bturn])

    check_cond()

    q = int(input())
    for _ in range(q) :
        r1, c1, r2, c2 = map(int, input().split())
        r1, c1, r2, c2 = r1-1, c1-1, r2-1, c2-1
        achange = Alice[r1][c1]
        bchange = Bob[r2][c2]
        if achange != bchange :
            Bob[r2][c2] = achange
            Alice[r1][c1] = bchange
            if achange == 'B' :
                AcntB -= 1
                if r1 == N - 1 :
                    sB.remove(c1)
                BcntA -= 1
                if r2 == N - 1 :
                    sA.remove(c2)

            else :
                BcntA += 1
                if r2 == N - 1 :
                    sA.add(c2)
                AcntB += 1
                if r1 == N - 1 :
                    sB.add(c1)

        check_cond()
sol_32249()