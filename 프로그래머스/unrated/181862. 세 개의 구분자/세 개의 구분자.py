def solution(myStr):
    answer = []
    string = ''
    for i in myStr : 
        if i in ['a', 'b', 'c'] :
            if string :
                answer.append(string)
            string = ''
        else : 
            string += i
                
    if string :
        answer.append(string)
        
    return answer if answer else ['EMPTY']