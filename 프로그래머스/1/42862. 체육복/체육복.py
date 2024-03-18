def solution(n, lost, reserve):
    answer = n
    lost = set(lost)
    reserve = set(reserve)
    
    reserve_and_lost = lost & reserve
    lost -= reserve_and_lost
    reserve -= reserve_and_lost
    
    for i in reserve :
        if i - 1 in lost :
            lost.remove(i - 1)
        elif i + 1 in lost :
            lost.remove(i + 1)
            
    answer -= len(lost)
    return answer

# def solution(n, lost, reserve):
#     lost_set = set(lost)
#     reserve_set = set(reserve)
#     answer = n

#     #여분이 있는데 도난당한 경우
#     reserve_and_lost = lost_set & reserve_set
#     lost_set -= reserve_and_lost
#     reserve_set -= reserve_and_lost

#     for x in reserve_set:
#         if x-1 in lost_set:
#             lost_set.remove(x-1)
#         elif x+1 in lost_set:
#             lost_set.remove(x+1)

#     answer -= len(lost_set)
#     return answer