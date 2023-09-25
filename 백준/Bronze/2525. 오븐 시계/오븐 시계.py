a, b = map(int, input().split())
c = int(input())
if b + c >= 60 :
    if a + ((b + c) // 60) >= 24 :
        a = a - 24 + ((b + c) // 60)
    else : 
        a += (b + c) // 60
    print(a, (b + c) % 60)
else :
    print(a, b+c)