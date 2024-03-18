def solution(answers) :
    # 수포자마다의 규칙을 정의
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    # 수포자 정답 리스트
    results = [0] * 3

    # 정답에 해당하는 키-값을 설정
    for i, answer in enumerate(answers) :
        # 각 수포자의 패턴을 키-값으로 설정
        for j, pattern in enumerate(patterns) :
            # 맞아 떨어지면
            if answer == pattern[i % len(pattern)] :
                # 각 수포자의 리스트에 +1
                results[j] += 1

    max_result = max(results)
    # 세 수포자의 정답을 가장 많이 맞춘 사람을 담는 리스트 생성
    highest_results = []
    
    for i, result in enumerate(results) :
        # 정답을 가장 많이 맞춘 사람이라면
        if result == max_result :
            # 최대 정답자를 정답 리스트에 삽입(리스트 0 부터 시작이니까 i+1)
            highest_results.append(i + 1)

    return highest_results