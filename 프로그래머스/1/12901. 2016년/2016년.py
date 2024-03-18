def solution(a, b):
    # 각 달에 해당하는 일 수를 기입 (0부터 12까지)
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # 2016년 1월 1일이 금요일이므로 금요일부터 시작하는 리스트 생성
    day = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    # 5월 24일이면 4월까지 다 더하고(0 ~ 4월까지 일 수를 다 더함) + 일을 더함
    total = sum(month[:a]) + b
    # 파이썬 인덱스는 0부터 시작이니까 total - 1을 기점으로 요일을 계산.
    answer = day[(total - 1) % 7]
    return answer