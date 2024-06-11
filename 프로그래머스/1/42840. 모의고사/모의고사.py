# 1. 패턴 찾기
# 2. 패턴을 찾았다면, 각 패턴으로 접근 시 몇 개가 매칭되는지 체크
# 3. 예외 사항 : 패턴 1의 경우 길이가 5이고, 문제가 6개 이상이라면 패턴 1의 길이보다 길어지게 되므로
# 넘어서는 정답은 패턴 1의 1번부터 다시 시작되는 알고리즘을 설계
def solution(answers):
    # 1. 수포자들의 패턴
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    # 2. 수포자들의 점수를 저장할 리스트
    results = [0] * 3
    
    # 3. 각 수포자의 패턴과 정답이 얼마나 일치하는지 확인
    for i, answer in enumerate(answers) :
        for j, pattern in enumerate(patterns) :
            if answer == pattern[i % len(pattern)] :
                results[j] += 1
    
    # 4. 가장 높은 점수 저장
    max_result = max(results)
    
    # 5. 가장 높은 점수를 가진 수포자들의 번호를 찾아서 리스트에 담음
    highest_score = []
    for i, result in enumerate(results) :
        if result == max_result :
            highest_score.append(i+1)

    return highest_score