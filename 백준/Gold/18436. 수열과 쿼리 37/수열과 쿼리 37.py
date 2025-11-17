import sys
import math
input = sys.stdin.readline

def init(lst, tree, node, start, end) :
    if start == end :
        if lst[start] % 2 == 0 :
            tree[node][0] = 1
        else :
            tree[node][1] = 1

    else :
        init(lst, tree, node * 2, start, (start + end) // 2)
        init(lst, tree, node * 2 + 1, (start + end) // 2 + 1, end)
        tree[node] = [tree[node*2][0] + tree[node*2+1][0], tree[node*2][1] + tree[node*2+1][1]]
    return tree[node]

def update(lst, tree, node, start, end, idx, val) :
    if idx < start or idx > end :
        return
    if start == end :
        if val % 2 == 0 :
            tree[node] = [1, 0]
        else :
            tree[node] = [0, 1]
        return tree[node]

    update(lst, tree, node*2, start, (start+end)//2, idx, val)
    update(lst, tree, node*2+1, (start+end)//2+1, end, idx, val)
    tree[node] = [tree[node*2][0] + tree[node*2+1][0], tree[node*2][1] + tree[node*2+1][1]]

def query(tree, node, start, end, left, right) :
    if left > end or right < start :
        return [0, 0]
    if left <= start and end <= right :
        return tree[node]
    l = query(tree, node*2, start, (start+end)//2, left, right)
    r = query(tree, node*2+1, (start+end)//2+1, end, left, right)

    return [l[0] + r[0], l[1] + r[1]]

N = int(input())
lst = list(map(int, input().split()))
h = math.ceil(math.log2(N))
tree_size = 1 << (h+1)
tree = [[0, 0] for _ in range(tree_size)]
init(lst, tree, 1, 0, N-1)

M = int(input())
for _ in range(M) :
    what, a, b = map(int, input().split())
    if what == 1 :
        if lst[a-1]%2 == b%2 :
            lst[a-1] = b
            continue
        else :
            update(lst, tree,1, 0, N-1, a-1, b)
            lst[a-1]=b

    elif what == 2 :
        print(query(tree, 1, 0, N-1, a-1, b-1)[0])

    elif what == 3 :
        print(query(tree, 1, 0, N-1, a-1, b-1)[1])