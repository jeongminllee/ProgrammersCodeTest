T = int(input())
def recursion(s, l, r) :
    global cnt
    cnt += 1
    if l >= r :
        return 1
    elif s[l] != s[r] :
        return 0
    else :
        return recursion(s, l+1, r-1)
def isPalindrome(s) :
    return recursion(s, 0, len(s) - 1)

for test_case in range(1, T + 1) :
    cnt = 0
    s = input()
    print(f"{isPalindrome(s)} {cnt}")