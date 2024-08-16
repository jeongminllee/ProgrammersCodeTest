# 스위치 상태를 변경하는 함수
def change(nums) :
    if switch[nums] == 0 :
        switch[nums] = 1
    else :
        switch[nums] = 0
    return

# 스위치 개수 입력
N = int(input())
# 스위치 상태 입력 (인덱스를 1부터 시작하기 위해 -1을 추가)
switch = [-1] + list(map(int, input().split()))
# 학생 수 입력
students = int(input())

# 각 학생에 대해 반복
for _ in range(students) :
    # 성별과 받은 수 입력
    gender, nums = map(int, input().split())
    
    # 남학생의 경우
    if gender == 1 :
        # 받은 수의 배수 위치에 있는 스위치 상태 변경
        for i in range(nums, N + 1, nums) :
            change(i)
    
    # 여학생의 경우
    else :
        # 받은 수 위치의 스위치 상태 변경
        change(nums)
        # 받은 수 위치를 중심으로 좌우 대칭인 구간 찾기
        for k in range(N // 2) :
            # 범위를 벗어나면 중단
            if nums + k > N or nums - k < 1 :
                break
            # 좌우 대칭이면 스위치 상태 변경
            if switch[nums + k] == switch[nums - k] :
                change(nums + k)
                change(nums - k)
            # 대칭이 아니면 중단
            else :
                break

# 최종 스위치 상태 출력
for i in range(1, N + 1) :
    print(switch[i], end=' ')
    # 20개씩 줄 바꿈
    if i % 20 == 0 :
        print()