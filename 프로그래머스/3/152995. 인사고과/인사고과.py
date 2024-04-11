def solution(scores):
    answer = 0
    wanho = scores[0]
    scores.sort(key=lambda x : (-x[0], x[1]))
    max_score1 = 0
    for score in scores :
        if score[0] > wanho[0] and score[1] > wanho[1] :
            return -1
        
        if score[1] >= max_score1 :
            max_score1 = score[1]
            if sum(wanho) < sum(score) :
                answer += 1
    return answer + 1