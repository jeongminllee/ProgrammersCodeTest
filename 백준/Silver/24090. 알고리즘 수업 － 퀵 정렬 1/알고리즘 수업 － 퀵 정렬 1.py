import sys
sys.setrecursionlimit(10**4)

def quick_sort(A, p, r) :
    if p < r :
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)

def partition(A, p, r) :
    global cnt, k
    x = A[r]
    i = p - 1
    for j in range(p, r) :
        if A[j] <= x :
            i += 1
            A[i], A[j] = A[j], A[i]
            cnt += 1
            
            if cnt == k :
                print(A[i], A[j])
                exit()
                
    if i + 1 != r :
        A[i + 1], A[r] = A[r], A[i + 1]
        cnt += 1
        
        if cnt == k :
            print(A[i + 1], A[r])
            exit()

    return i + 1

n, k = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0

quick_sort(A, 0, n - 1)

if k > cnt :
    print(-1)