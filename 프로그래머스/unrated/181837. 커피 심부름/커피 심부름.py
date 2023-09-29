def solution(order):
    answer = 0
    order_dict = {"americano" : 4500, "cafelatte" : 5000}
    for i in order :
        if "ice" in i :
            i = i.replace("ice", "")
        if "hot" in i :
            i = i.replace("hot", "")
        if "anything" in i :
            i = i.replace("anything", "americano")
        
        if i in order_dict :
            answer += order_dict[i]
    return answer

def solution(order) :
    answer = 0
    for i in order :
        if 'latte' in i :
            answer += 5000
        else :
            answer += 4500
    return answer