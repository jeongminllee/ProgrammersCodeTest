s = input().lower()
# ord('a') = 97
syms = ['@', '8', '(', '|)', '3', '#', '6', '[-]', '|', '_|', '|<', '1', '[]\/[]', '[]\[]', '0', '|D', '(,)', '|Z', '$', "']['", '|_|', '\/', '\/\/', '}{', '`/', '2']
'''
res = ''

for char in s :
    if char.isalpha() :
        res += syms[ord(char) - 97]
    else :
        res += char
print(res)
'''
print(''.join(syms[ord(c) - 97] if c.isalpha() else c for c in s))