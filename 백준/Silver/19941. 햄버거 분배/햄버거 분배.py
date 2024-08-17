# P : 사람, H : 햄버거
N, K = map(int, input().split())
lst = list(input().rstrip())
ans = 0

for i in range(N) :             # 테이블을 돌아다니며
    if lst[i] == "P" :          # 사람일 경우
        for j in range(max(i - K, 0), min(i + K + 1, N)) :  # 사람 손에 닿는 햄버거는
            if lst[j] == "H" :                              # H 를 찾음
                lst[j] = "O"                                # 먹는다
                ans += 1                                    # 그 사람 인원수 추가
                break
                
print(ans)