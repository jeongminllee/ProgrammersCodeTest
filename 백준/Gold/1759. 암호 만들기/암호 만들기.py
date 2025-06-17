L, C = map(int, input().split())
lst = input().split()
lst.sort()

aeiou = ('a', 'e', 'i', 'o', 'u')

# 최소 한개의 모음, 최소 두개의 자음
def check(arr) :
    a_cnt, c_cnt = 0, 0 # 모음 개수, 자음 개수

    for a in arr :
        if a in aeiou :
            a_cnt += 1
        else :
            c_cnt += 1

    if a_cnt >= 1 and c_cnt >= 2 :
        return True
    else :
        return False
    
def backtrack(arr) :
    if len(arr) == L :
        if check(arr) :
            print(''.join(arr))
            return

    for i in range(len(arr), C) :
        if arr[-1] < lst[i] :
            arr.append(lst[i])
            backtrack(arr)
            arr.pop()

for i in range(C - L + 1) :
    a = [lst[i]]
    backtrack(a)