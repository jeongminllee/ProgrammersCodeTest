def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs :
        ans = [i[s : s + l]]
        for a in ans :
            if int(a) > k :
                answer.append(int(a))
    return answer