import sys
input = sys.stdin.readline
sys.setrecursionlimit(20000)

preorder = []
while True:
    try:
        preorder.append(int(input()))          
    except:
        break

def postorder(start, end):
    if start >= end-1:
        print(preorder[start])
        return
    
    if preorder[start] > preorder[end-1] or preorder[start] < preorder[start+1]:
        postorder(start+1, end)
        print(preorder[start])
        return
    
    mid = 0
    for i in range(start+1, end):
        if preorder[start] < preorder[i]:
            mid = i
            break

    postorder(start+1, mid)
    postorder(mid, end)
    print(preorder[start])
    
postorder(0, len(preorder))