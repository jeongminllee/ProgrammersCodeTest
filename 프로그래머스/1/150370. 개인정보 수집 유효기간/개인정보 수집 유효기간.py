def solution(today, terms, privacies):
    answer = []
    d = {}
    today_lst = list(map(int, today.split('.')))
    for term in terms :
        n ,m = term.split()
        d[n] = int(m) * 28
        
    for i in range(len(privacies)) :
        date, s = privacies[i].split()
        date_lst = list(map(int, date.split('.')))
        yyyy = (today_lst[0] - date_lst[0])*12*28
        mm = (today_lst[1] - date_lst[1])*28
        dd = today_lst[2] - date_lst[2]
        valid_date = yyyy + mm + dd
        if d[s] <= valid_date :
            answer.append(i+1)
    return answer