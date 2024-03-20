# 백트래킹(완전탐색)
# 가능한 모든 경우 => 정답!
# n(종료조건) : 날짜(idx)
# n >= N : 종료!
# ans = 0
# dfs(n, sm)
# 종료 if n >= N :	# 종료조건
# ans = max(ans, sm)
# return

# 하부 호출
# if n + T[n] <= N : 	# 상담
# 	dfs(n + T[n], sm + P[n])
# dfs(n + 1, sm)	# 상담 x

def dfs(n, sm) :
	global ans
	# [1] 종료 조건 : 가능한 n을 종료에 관련된 것으로 정의!
	if n >= N :
		ans = max(ans, sm)
		return

	# [2] 하부 호출 : 화살표 개수만큼 호출
	if n + T[n] <= N :		# 상담하는 경우 (퇴사일 전 완료 가능할 때만 상담)
		dfs(n + T[n], sm + P[n])
	dfs(n + 1, sm)			# 상담하지 않는 경우(항상 가능)
	
N = int(input())
T = [0] * N
P = [0] * N
for i in range(N) :
	T[i], P[i] = map(int, input().split())

ans = 0
dfs(0, 0)
print(ans)