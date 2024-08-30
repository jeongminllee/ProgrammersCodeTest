N=int(input())

adj=[[] for _ in range(N+1)]
#adj[v]:v와 간선으로 연결된 정점들의 모임
for _ in range(N-1):
    a,b=map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

p=[0 for _ in range(N+1)]#p[V]:V의 부모 정점 번호
sz=[1 for _ in range(N+1)]
#sz[V]:V를 루트로 하는 서브트리의 크기

stack=[1]
dfsord=[]
while stack:
    cur=stack.pop()
    dfsord.append(cur)
    for nxt in adj[cur]:
        if nxt == p[cur]:
            continue
        p[nxt]=cur
        stack.append(nxt)

while dfsord:
    v=dfsord.pop()
    sz[p[v]]+=sz[v]
            

ans=0
MM=N*(N-1)//2
for i in range(2,N+1):
    t=N-sz[i] 
    #루트와 연결 했을 때 i와 i의 부모를 잇는 간선을 지나지 않는 정점의 수
    ans+= MM-t*(t-1)//2

print(ans)
