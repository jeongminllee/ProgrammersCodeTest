import sys
sys.setrecursionlimit(10**4)

def postorder(tree) :
    if not tree :
        return []

    root = tree[0]
    root_left = [x for x in tree[1:] if x < root]
    root_right = [x for x in tree[1:] if x > root]

    return postorder(root_left) + postorder(root_right) + [root]

tree = []
while True :
    try :
        a = int(input())
        tree.append(a)
    except :
        break

for node in postorder(tree) :
    print(node)