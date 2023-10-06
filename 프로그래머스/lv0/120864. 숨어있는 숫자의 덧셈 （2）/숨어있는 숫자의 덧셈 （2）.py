import re

def solution(my_string):
    return sum([int(n) for n in re.findall('\d+', my_string)])



# def solution(my_string):
#     s = ''.join(i if i.isdigit() else ' ' for i in my_string)
#     return sum(int(n) for n in s.split())