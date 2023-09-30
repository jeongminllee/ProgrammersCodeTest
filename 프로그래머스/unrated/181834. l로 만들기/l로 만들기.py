def solution(myString):
    for string in myString :
        if ord(string) < ord('l') :
            myString = myString.replace(string, 'l')
    return myString