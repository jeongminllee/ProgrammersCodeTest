N, B = map(int, input().split())
res = ''
while N > 0 :
    remainder = N % B
    if remainder <= 9 :
        res += str(remainder)
    else :
        str_remainder = chr(remainder + ord("A") - 10)
        res += str_remainder
    N //= B

print(res[::-1])