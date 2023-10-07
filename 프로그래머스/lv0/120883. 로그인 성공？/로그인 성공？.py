def solution(id_pw, db):
    answer = ''
    for i in range(len(db)) :
        if id_pw == db[i] :
            return 'login'
        elif id_pw[0] == db[i][0] and id_pw[1] != db[i][1] :
            return 'wrong pw'
    return 'fail'