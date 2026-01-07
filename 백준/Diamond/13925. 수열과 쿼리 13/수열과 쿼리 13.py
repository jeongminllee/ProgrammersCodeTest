
MOD = 10 ** 9 + 7

class SegmentTree :
    def __init__(self, a):
        self.n = len(a)
        self.a = a[:]
        self.tree = [0] * (4 * self.n)
        self.lazy_mul = [1] * (4 * self.n)
        self.lazy_add = [0] * (4 * self.n)
        self._init(A, 1, 0, self.n-1)

    def _init(self, A, node, start, end):
        if start == end :
            self.tree[node] = A[start] % MOD
            return
        mid = (start + end) // 2
        self._init(A, node*2, start, mid)
        self._init(A, node*2+1, mid+1, end)
        self.tree[node] = (self.tree[node*2] + self.tree[node*2+1]) % MOD

    def _push(self, node, start, end):
        if self.lazy_mul[node] == 1 and self.lazy_add[node] == 0 :
            return
        mul = self.lazy_mul[node]
        add = self.lazy_add[node]

        self.tree[node] = (self.tree[node] * mul + (end - start + 1) * add) % MOD

        if start != end :
            for child in (node * 2, node * 2 + 1) :
                self.lazy_mul[child] = (self.lazy_mul[child] * mul) % MOD
                self.lazy_add[child] = (self.lazy_add[child] * mul + add) % MOD

        self.lazy_mul[node] = 1
        self.lazy_add[node] = 0


    def update(self, l, r, mul, add):
        self._update(1, 0, self.n-1, l, r, mul, add)
    def _update(self, node, start, end, l, r, mul, add):
        self._push(node, start, end)

        if r < start or l > end :
            return

        if l <= start and r >= end :
            self.lazy_mul[node] = mul
            self.lazy_add[node] = add
            self._push(node, start, end)
            return

        mid = (start + end) // 2
        self._update(node*2, start, mid, l, r, mul, add)
        self._update(node*2+1, mid+1, end, l, r, mul, add)
        self.tree[node] = (self.tree[node*2] + self.tree[node*2+1]) % MOD

    def query(self, left, right) :
        return self._query(1, 0, self.n-1, left, right)

    def _query(self, node, start, end ,left, right):
        self._push(node, start, end)

        if left > end or right < start :
            return 0

        if left <= start and right >= end :
            return self.tree[node]

        mid = (start + end) // 2
        return (self._query(node * 2, start, mid, left ,right)
                + self._query(node * 2 + 1, mid + 1, end, left, right)
                ) % MOD



N = int(input())
A = list(map(int, input().split()))
seg = SegmentTree(A)

M = int(input())
for _ in range(M):
    q = list(map(int, input().split()))
    if q[0] == 1 :
        i, x, y, v = q
        seg.update(x - 1, y - 1, 1, v)
    elif q[0] == 2 :
        i, x, y, v = q
        seg.update(x - 1, y - 1, v, 0)

    elif q[0] == 3 :
        i, x, y, v = q
        seg.update(x - 1, y - 1, 0, v)

    else :
        i, x, y = q
        print(seg.query(x - 1, y - 1))
