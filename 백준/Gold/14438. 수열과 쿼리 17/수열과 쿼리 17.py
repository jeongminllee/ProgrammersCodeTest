import math

def init(arr, tree, node, start, end) :
    if start == end :
        tree[node] = arr[start]
    else :
        mid = (start + end) // 2
        init(arr, tree, node*2, start, mid)
        init(arr, tree, node*2+1, mid+1, end)
        tree[node] = min(tree[node*2], tree[node*2+1])

def update(arr, tree, node, start, end, idx, val) :
    if idx < start or idx > end :   # 구간 밖
        return
    if start == end :
        arr[idx] = val
        tree[node] = val
        return
    mid = (start + end) // 2
    update(arr, tree, node*2, start, mid, idx, val)
    update(arr, tree, node*2+1, mid+1, end, idx, val)
    tree[node] = min(tree[node*2], tree[node*2+1])

def query(arr, tree, node, start, end, left, right) :
    if left > end or right < start :    # 구간 밖
        return -1
    if left <= start and right >= end :
        return tree[node]
    mid = (start + end) // 2
    lmin = query(arr, tree, node*2, start, mid, left, right)
    rmin = query(arr, tree, node*2+1, mid+1, end, left, right)
    if lmin == -1 :
        return rmin
    elif rmin == -1 :
        return lmin
    else :
        return min(lmin, rmin)

if __name__ == "__main__" :
    N = int(input())
    arr = list(map(int, input().split()))
    M = int(input())

    h = math.ceil(math.log2(N))
    tree_size = 1<<(h+1)
    tree = [0] * tree_size
    init(arr, tree, 1, 0, N-1)
    for _ in range(M) :
        kind, a, b = map(int, input().split())
        if kind == 1 :
            idx, val = a-1, b
            update(arr, tree, 1, 0, N-1, idx, val)
        else :
            left, right = a-1, b-1
            print(query(arr, tree, 1, 0, N-1, left, right))
