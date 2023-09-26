def solution(rny_string):
    answer = ''.join(["rn" if i == "m" else i for i in rny_string])
    return answer