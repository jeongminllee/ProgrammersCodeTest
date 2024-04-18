words = []

while True :
    word = input().rstrip()
    if word == '.' :
        break
    words.append(word)

for word in words :
    stack = []
    for i in word :
        if i == "(" :
            stack.append(i)
        elif i == "[" :
            stack.append(i)
        elif i == ")" :
            if stack and stack[-1] == "(" :
                stack.pop()
            else :
                print("no")
                break

        elif i == "]" :
            if stack and stack[-1] == "[" :
                stack.pop()
            else :
                print("no")
                break

    else :
        if not stack :
            print("yes")
        else :
            print("no")