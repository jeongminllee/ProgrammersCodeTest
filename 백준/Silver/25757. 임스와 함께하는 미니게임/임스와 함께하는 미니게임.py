N, P = input().split()
N = int(N)

# game : 임스와 같이 게임 하기 때문에 -1 씩 시켜주어야 한다.
game = {"Y" : 2, "F" : 3, "O" : 4}
limit = game[P] - 1

# 한 번 같이 플레이한 사람과는 다시 플레이 하지 않는다. => 중복 제거
players = set()

for _ in range(N) :
    players.add(input())

ans = len(players) // limit
print(ans)