# def peil(s) :
#     i, j = 0, len(s) - 1
#     while i<j :
#         if s[i] == s[j] :
#             i += 1
#             j -= 1
#         else :
#             return 'no'
#     return 'yes'

def peil(s) :
    return s == s[::-1]

while True :
    s = input()
    if s == '0' :
        break
    print('yes' if peil(s) else 'no')