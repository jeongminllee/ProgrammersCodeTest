alpha = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbol = [' ', '@', '8', '(', '|)', '3', '#', '6', '[-]', '|', '_|', '|<', '1', '[]\/[]', '[]\[]', '0', '|D', '(,)', '|Z', '$', "']['", '|_|', '\/', '\/\/', '}{', '`/', '2']

k = input().lower()

answer = ''

for character in k:
    if character in alpha:
        answer += symbol[alpha.index(character)]
    else:
        answer += character

print(answer)