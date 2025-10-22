import math

def init(lst: list, tree: list, node: int, start: int, end: int) -> None :
    if start == end :
        val = lst[start]
        tree[node] = [val, val]
        return

    else :
        init(lst, tree, node*2, start, (start + end) // 2)
        init(lst, tree, node*2+1, (start + end)//2+1, end)
        tree[node] = [min(tree[node*2][0], tree[node*2+1][0]), max(tree[node*2][1], tree[node*2+1][1])]

def query(tree: list, node: int, start: int, end: int, left: int, right: int) -> tuple:
    if left > end or right < start :
        return [10 ** 10, 0]
    if left <= start and end <= right :
        return tree[node]
    lmin, lmax = query(tree, node*2, start, (start+end)//2, left, right)
    rmin, rmax = query(tree, node*2+1, (start+end)//2+1, end, left, right)

    return [min(lmin, rmin), max(lmax, rmax)]
if __name__ == "__main__" :
    N, M = map(int, input().split())

    arr1 = []  # init tree

    for _ in range(N) :
        arr1.append(int(input()))

    h = math.ceil(math.log2(N))
    tree_size = 1 << (h+1)
    tree = [0] * tree_size
    init(arr1, tree, 1, 0, N-1)


    for _ in range(M) :
        t1, t2 = map(int, input().split())
        print(*query(tree, 1, 0, N-1, t1-1, t2-1))