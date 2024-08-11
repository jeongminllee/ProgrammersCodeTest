from sys import setrecursionlimit
import io

# 재귀 깊이 제한을 늘립니다. 이는 깊은 트리 구조를 처리하기 위해 필요합니다.
setrecursionlimit(100500)

# 빠른 입력을 위해 버퍼 크기가 큰 BufferedReader를 사용합니다.
input = io.BufferedReader(io.FileIO(0), 1<<18).readline

# 테스트 케이스의 수를 입력받습니다.
t = int(input())

# 문제의 제약 조건에 따른 최대 도시 수와 최대 인구 수를 상수로 정의합니다.
M_N = 100000  # 최대 도시 수
M_X = 1000000000  # 최대 인구 수

# 트리 구조를 저장할 리스트를 초기화합니다. 각 도시의 연결 정보를 저장합니다.
tree = [[] for _ in range(M_N+1)]

def dfs(v):
    '''
    깊이 우선 탐색을 통해 트리 구조를 탐색하고 부모 노드를 기록합니다.
    :param v: 현재 탐색 중인 노드(도시)
    '''
    for u in tree[v]:
        if vis[u] == 0:  # 아직 방문하지 않은 노드라면
            vis[u] = 1  # 방문 표시
            p[u] = v  # 부모 노드 기록
            dfs(u)  # 재귀적으로 탐색 계속

def f(v, x):
    '''
    현재 노드 v에서 시작하는 서브트리에 대해 검역소 설치 개수와 총 인구수를 계산합니다.
    :param v: 현재 노드(도시)
    :param x: 한 그룹의 최대 허용 인구수
    :return: (필요한 검역소 수, 현재 서브트리의 총 인구수)
    '''
    tmp = []  # 자식 노드들의 인구수를 저장할 리스트
    c, total = 0, 0  # c: 필요한 검역소 수, total: 현재까지의 총 인구수
    for u in tree[v]:
        if p[u] != v:  # u가 v의 자식 노드가 아니면 건너뜁니다
            continue
        val = f(u, x)  # 재귀적으로 자식 노드의 결과를 얻습니다
        c += val[0]  # 검역소 수 누적
        total += val[1]  # 인구수 누적
        tmp.append(val[1])  # 자식 노드의 인구수 저장
    
    tmp.sort()  # 인구수를 오름차순으로 정렬
    while tmp and total + a[v] > x:  # 현재 그룹의 인구수가 x를 초과하면
        c += 1  # 검역소 추가
        total -= tmp.pop()  # 가장 큰 인구수를 가진 자식을 분리
    return c, total + a[v]  # (필요한 검역소 수, 현재 그룹의 총 인구수) 반환

for _ in range(t):  # 각 테스트 케이스에 대해
    n, k = map(int, input().split())  # 도시 수 n과 설치 가능한 검역소 수 k 입력
    a = [0]+list(map(int, input().split()))  # 각 도시의 인구수 입력 (1-indexed)
    
    # 트리 초기화
    for i in range(M_N+1): 
        tree[i].clear()
        
    # 트리 구축: 각 도로 정보를 입력받아 트리 구조 생성
    for _ in range(n-1):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)
    
    # 부모 노드와 방문 여부 초기화
    p = [0]*(n+1)  # 각 노드의 부모 노드 정보
    vis = [0]*(n+1)  # 각 노드의 방문 여부
    vis[1] = 1  # 루트 노드(1번 도시) 방문 표시
    dfs(1)  # 깊이 우선 탐색으로 트리 구조 파악

    # 이진 탐색으로 최적의 해 찾기
    l, r = max(a), M_X*n  # 탐색 범위: 최대 도시 인구수 ~ 가능한 최대 총 인구수
    while l < r:
        mid = (l+r) // 2  # 중간값 계산
        tmp = f(1, mid)[0]  # 현재 중간값으로 필요한 검역소 수 계산
        if tmp <= k:  # 필요한 검역소 수가 k 이하면
            r = mid  # 상한을 낮춤
        else:  # 필요한 검역소 수가 k보다 크면
            l = mid+1  # 하한을 높임
    
    print(l)  # 최종적으로 찾은 최소 치료제 수 출력