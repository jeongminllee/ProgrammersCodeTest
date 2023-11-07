def solution(id_list, report, k):
    answer = [0] * len(id_list)
    dct = {id : [] for id in id_list}
    for i in set(report) :
        i = i.split()
        dct[i[1]].append(i[0])

    for key, val in dct.items() :
        if len(val) >= k :
            for v in val :
                answer[id_list.index(v)] += 1
    return answer