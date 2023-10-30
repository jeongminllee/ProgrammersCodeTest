N = input()
char = ''
for i in N :
    if ord(i) < 68 :
        char += chr(ord(i)+23)
    else :
        char += chr(ord(i)-3)

print(char)