'''
nn = max 10 ** 14
n = 10 ** 7
left // n = 0 1 2 ... => 첫 숫자의 인덱스 
0 => 1 2 3 4 ... n
1 => 2 2 3 4 ... n
2 => 3 3 3 4 ... n
for i in range(n)
'''
def solution(n, left, right):
    return [max(i // n, i % n) + 1 for i in range(left, right + 1)]