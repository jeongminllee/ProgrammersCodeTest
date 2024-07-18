import sys
sys.setrecursionlimit(10**4)

def postorder(tree, s, e) :
    if s > e :
        return []

    root = tree[s]

    left = s + 1
    right = e
    while left <= right :
        mid = (left + right) // 2
        if tree[mid] > root :
            right = mid - 1
        else :
            left = mid + 1

    left_tree = postorder(tree, s + 1, right)

    right_tree = postorder(tree, right + 1, e)

    return left_tree + right_tree + [root]

tree = []
while True :
    try :
        a = int(input())
        tree.append(a)
    except :
        break

for node in postorder(tree, 0, len(tree) - 1) :
    print(node)