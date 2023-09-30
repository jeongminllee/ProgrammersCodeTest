def solution(my_string):
    reject = 'a', 'e', 'i', 'o', 'u'
    
    for i in my_string :
        if i in reject :
            my_string = my_string.replace(i, "")
            
    return my_string