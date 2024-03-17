# if a in (1, 3, 5, 7, 8, 10, 12) => 31
# elif a in (4, 6, 9, 11) => 30
# else => 29
# a, b = 1, 1 => FRI
# (a * i + b) % 7 => 을 리턴하면 되지 않을까?

def solution(a, b):
    answer = ''
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    total = sum(month[:a]) + b
    answer = day[(total - 1) % 7]
    return answer