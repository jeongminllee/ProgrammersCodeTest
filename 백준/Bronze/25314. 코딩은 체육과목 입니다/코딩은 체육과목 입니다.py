a = int(input())
b = 0

if a % 4 == 0 :
    b = a // 4
else :
    b = a // 4 + 1
    
print(b * "long " + "int")