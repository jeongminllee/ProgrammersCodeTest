# 소문자 알파벳으로만 이루어져 있기 때문에 ord, chr 는 안 써도 될듯
# strings[i][n] 이 통하는지 확인해보고 이걸로 진행
# 근데 저 사전순으로 정렬한다는 건 무슨 의밀까? abcd, abce 정렬해봐야겠다.
def solution(strings, n):
    return sorted(strings, key=lambda x:(x[n], x))
# lambda의 return 값을 튜플 형태로 하게 되면, x[n] 을 1번, x를 2번 순위로 비교하여 입력을 하게 됨.