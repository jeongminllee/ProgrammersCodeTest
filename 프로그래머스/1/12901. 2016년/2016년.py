def solution(a, b):
    answer = ''
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    total = sum(month[:a]) + b
    answer = day[(total - 1) % 7]
    return answer