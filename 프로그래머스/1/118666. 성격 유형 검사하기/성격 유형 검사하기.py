# survey : "RT", "TR", "FC", "CF", "MJ", "JM", "AN", "NA"
# AN = 5 네오형 약간 동의
# NA = 5 어피치형 약간 동의 이런거구나
# 동점이면 사전순으로 빠른 순으로 나타내고

def solution(survey, choices):
    dct = {
        'R' : 0,
        'T' : 0,
        'C' : 0,
        'F' : 0,
        'J' : 0,
        'M' : 0,
        'A' : 0,
        'N' : 0
           }

    for i in range(len(survey)) :
        if choices[i] >= 4 :
            dct[survey[i][1]] += choices[i] - 4

        elif choices[i] < 4 :
            dct[survey[i][0]] += 4 - choices[i]

    # print(dct)
    answer = ''
    if dct['R'] >= dct['T'] :
        answer += 'R'
    else :
        answer += 'T'

    if dct['C'] >= dct['F'] :
        answer += 'C'
    else :
        answer += 'F'

    if dct['J'] >= dct['M'] :
        answer += 'J'
    else :
        answer += 'M'

    if dct['A'] >= dct['N'] :
        answer += 'A'
    else :
        answer += 'N'

    return answer