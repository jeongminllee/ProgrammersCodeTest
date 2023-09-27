def solution(rank, attendance):
    temp = []
    for i, ranker in enumerate(rank) :
        if attendance[i] == 1 :
            temp.append([rank[i], i])
            
    temp.sort(key = lambda v : v[0])
    return 10000 * temp[0][1] + 100 * temp[1][1] + temp[2][1]