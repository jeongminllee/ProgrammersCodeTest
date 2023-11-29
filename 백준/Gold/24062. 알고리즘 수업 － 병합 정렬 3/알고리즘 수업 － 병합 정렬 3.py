import sys

def merge(arr, p, q, r) :
    global n, idx
    tmp = []
    i = p
    j = q + 1
    while True :
        if i > q or j > r :
            break
        if arr[i] <= arr[j] :
            tmp.append(arr[i])
            i += 1
        else :
            tmp.append(arr[j])
            j += 1
            
    while True :
        if i > q :
            break
        tmp.append(arr[i])
        i += 1
        
    while True :
        if j > r :
            break
        tmp.append(arr[j])
        j += 1
        
    a = p
    b = 0
    
    while True :
        if a > r :
            break
        arr[a] = tmp[b]
        
        if a <= idx and arr[a] != tmp[b] :
            print(0)
            sys.exit()
            
        if arr[a] == B[a] :
            search = idx
            for i in range(search, n) :
                if arr[i] == B[i] :
                    idx = i
                if arr[i] != B[i] :
                    break
                elif i == n - 1 :
                    print(1)
                    sys.exit()
                    
        a += 1
        b += 1
    
def merge_sort(arr, p, r) :
    if p < r :
        q = (p + r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q + 1, r)
        merge(arr, p, q, r)
        
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
idx = -1

if A == B:
    print(1)
    sys.exit()
    
merge_sort(A, 0, n - 1)

print(0)