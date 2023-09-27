def solution(emergency):
    answer = []
    temp = sorted(emergency, reverse = True)
    
    for i in emergency :
        print(i, end = " -> ")
        print("%d등"%(temp.index(i) + 1), end = " ")
        answer.append(temp.index(i) + 1)
    return answer