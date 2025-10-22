import math

MOD = 1_000_000_007
def init(arr, tree, node, start, end) :
    if start == end :
        tree[node] = arr[start]

    else :
        mid = (start+end) // 2
        init(arr, tree, node*2, start, mid)
        init(arr, tree, node*2+1, mid+1, end)
        tree[node] = (tree[node*2] * tree[node*2+1])%MOD

def update(arr, tree, node, start, end, idx, val) :
    if idx < start or idx > end :
        return
    if start == end :
        arr[idx] = val
        tree[node] = val
        return
    mid = (start + end) // 2
    update(arr, tree, node*2, start, mid, idx, val)
    update(arr, tree, node*2+1, mid+1, end, idx, val)
    tree[node] = (tree[node*2] * tree[node*2+1])%MOD

def query(tree, node, start, end, left, right) :
    if left > end or right < start :
        return 1
    if left <= start and end <= right :
        return tree[node]
    mid = (start + end) // 2
    lmul = query(tree, node*2, start, mid, left, right)
    rmul = query(tree, node*2+1, mid+1, end, left, right)
    return (lmul * rmul)%MOD


if __name__ == "__main__" :
    N, M, K = map(int, input().split())
    arr = [int(input()) for _ in range(N)]

    h = math.ceil(math.log2(N))
    tree_size = 1<<(h+1)
    tree = [0] * tree_size
    init(arr, tree, 1, 0, N-1)

    for _ in range(M+K) :
        kind, a, b = map(int, input().split())
        if kind == 1 :
            update(arr, tree, 1, 0, N-1, a-1, b)
        else :
            print(query(tree, 1, 0, N-1, a-1, b-1)%MOD)