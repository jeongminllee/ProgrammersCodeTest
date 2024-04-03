def solution(s):
    # [1] 문자열 s를 파싱하여 리스트로 변환
    answer = []
    s = s[2:-2].split("},{")
    s = sorted(s, key=len)
    
    # [2] 각 원소를 순회하면서 이전 원소와 차이나는 부분을 구함.
    for nums in s :
        nums = nums.split(',')
        for num in nums :
            num = int(num)
            if num not in answer :
                answer.append(num)
    return answer