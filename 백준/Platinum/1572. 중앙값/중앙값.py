import math

def merge(a, b) :
    return a + b        # 개수 합

IDENTITY = 0
MAX_VALUE = 65536

def init(arr, tree, node, start, end) :
    if start == end :
        tree[node] = arr[start]
        return
    mid = (start + end) // 2
    init(arr, tree, node, start, mid)
    init(arr, tree, node, mid+1, end)
    tree[node] = merge(tree[node*2], tree[node*2+1])

def update(tree, node, start, end, idx, value) :
    if idx < start or idx > end :
        return
    if start == end :
        tree[node] += value
        return

    mid = (start + end) // 2
    update(tree, node*2, start, mid, idx, value)
    update(tree, node*2+1, mid+1, end, idx, value)
    tree[node] = merge(tree[node*2], tree[node*2+1])

def query(tree, node, start, end, left, right) :
    # 여기서는 left = K, right는 사용하지 않음
    if start == end :
        return start

    mid = (start + end) // 2
    if tree[node*2] >= left :
        return query(tree, node*2, start, mid, left, right)
    else :
        return query(tree, node*2+1, mid+1, end, left - tree[node*2], right)

N, K = map(int, input().split())
nums = [0] * (N+1)

for i in range(1, N+1) :
    nums[i] = int(input())

size = 1
while size <= MAX_VALUE :
    size <<= 1

arr = [0] * size
tree = [0] * (size * 2)

init(arr, tree, 1, 0, size - 1)

# 처음 K-1개 추가
for i in range(1, K) :
    update(tree, 1, 0, size-1, nums[i], 1)

res = 0

for i in range(K, N+1) :
    update(tree, 1, 0, size-1, nums[i], 1)
    res += query(tree, 1, 0, size-1, (K+1)//2, 0)
    update(tree, 1, 0, size-1, nums[i - (K - 1)], -1)

print(res)