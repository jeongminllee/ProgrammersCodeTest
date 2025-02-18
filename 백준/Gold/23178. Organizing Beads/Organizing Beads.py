import sys
input = sys.stdin.readline

class Fenw :
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, delta):
        # BIT의 i번째 인덱스에 delta 만큼 추가
        while i <= self.n :
            self.tree[i] += delta
            i += i & -i

    def query(self, i):
        # 1부터 i까지의 누적합 반환
        s = 0
        while i :
            s += self.tree[i]
            i -= i & -i
        return s

    def find(self, v):
        # 누적합이 v 이상이 되는 가장 작은 인덱스를 찾음
        idx = 0
        bit_mask = 1 << (self.n.bit_length() - 1)
        while bit_mask :
            t = idx + bit_mask
            if t <= self.n and self.tree[t] < v :
                v -= self.tree[t]
                idx = t
            bit_mask //= 2
        return idx + 1

def sol_23178() :
    n = int(input())    # the length of the bead barrel.
    berral = input().strip()  # berral
    q = int(input())    # Query

    # BIT를 이용하여 구슬의 위치를 관리
    BIT = Fenw(n)
    # 각 칸에 구슬이 있는지 상태를 저장(1-indexed)
    state = [False] * (n + 1)

    # 초기 구슬 상태 세팅
    for i, ch in enumerate(berral, start=1) :
        if ch == 'O' :
            state[i] = True
            BIT.update(i, 1)

    # 각 쿼리마다 구슬 추가/제거 후, 답을 계산
    # 답 = min(r - k, n - l + 1 - k)
    #   -k: 현재 구슬의 총 개수
    #   -l: 가장 왼쪽의 구슬 위치 (BIT.find(1))
    #   -r: 가장 오른쪽 구슬의 위치(BIT.find(k))
    output_lines = []
    for _ in range(q) :
        k = int(input())
        if state[k] :
            # 구슬이 있으면 제거
            state[k] = False
            BIT.update(k, -1)
        else :
            # 구슬이 없으면 추가
            state[k] = True
            BIT.update(k, 1)

        total = BIT.query(n)    # 현재 구슬의 총 개수, 문제에서는 0이 되지 않음이 보장
        l = BIT.find(1)         # 가장 왼쪽에 있는 구슬의 위치
        r = BIT.find(total)     # 가장 오른쪽에 있는 구슬의 위치

        # 왼쪽으로 모으려면 r번 구슬을 k번 자리까지 옮겨야 하므로 r - total
        # 오른쪽으로 모으려면 l번 구슬을 n - total + 1 자리로 옮겨야 하므로 n - l + 1 - total
        ans = min(r - total, n - l + 1 - total)
        print(str(ans))

sol_23178()