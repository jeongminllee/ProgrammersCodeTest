def check(num) :
    if num == 1 :
        return False

    for i in range(2, int(num ** (1/2)) + 1) :
        if num % i == 0 :
            return False
    return True

N = int(input())
lst = list(map(int, input().split()))
ans = 0

for num in lst :
    if check(num) :
        ans += 1
print(ans)

'''
def check(num) :
    if num == 1 :
        return False

    for i in range(2, num) :
        if num % i == 0 :
            return False
    return True

N = int(input())
lst = list(map(int, input().split()))
ans = 0

for num in lst :
    if check(num) :
        ans += 1
print(ans)
'''