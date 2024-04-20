def solution(people, limit):
    answer = 0      # 필요한 보트 개수
    people.sort()   # 몸무게를 오름차순으로 정렬
    i = 0           # 가장 가벼운 사람을 가리키는 인덱스
    j = len(people) - 1 # 가장 무거운 사람을 가리키는 인덱스

    while i <= j :  # 가장 무거운 사람과 가장 가벼운 사람을 같이 태울 수 있으면 두 사람 모두 보트에 태움
        if people[j] + people[i] <= limit :
            i += 1
        # 무거운 사람만 태울 수 있으면 무거운 사람만 보트에 태움
        j -= 1
        answer += 1
    # [0,3], [0,2], [0,1 => 1,1 => 1,0] => return
    return answer