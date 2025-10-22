import math

def init(lst, tree, node, start, end) :
    if start == end :
        tree[node] = lst[start]

    else :
        mid = (start + end) // 2
        init(lst, tree, node*2, start, mid)
        init(lst, tree, node*2+1, mid+1, end)
        tree[node] = min(tree[node*2], tree[node*2+1])

def query(lst, tree, node, start, end, left, right) :
    if left > end or right < start :
        return -1
    if left <= start and right >= end :
        return tree[node]
    mid = (start + end) // 2
    lmin = query(lst, tree, node*2, start, mid, left, right)
    rmin = query(lst, tree, node*2+1, mid+1, end, left, right)

    if lmin == -1 :
        return rmin
    elif rmin == -1 :
        return lmin
    else :
        return min(lmin, rmin)


if __name__ == "__main__" :
    N, M = map(int, input().split())
    lst = [int(input()) for _ in range(N)]

    h = math.ceil(math.log2(N)) + 1
    tree_size = 1 << h
    tree = [0] * tree_size
    init(lst, tree, 1, 0, N-1)

    for _ in range(M) :
        a, b = map(int, input().split())
        print(query(lst, tree, 1, 0, N-1, a-1, b-1))