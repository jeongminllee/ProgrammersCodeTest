def solution(rny_string):
    answer = ''.join(["rn" if i == "m" else i for i in rny_string])
    return answer


def solution(rny_string) :
    return rny_string.replace('m', 'rn')