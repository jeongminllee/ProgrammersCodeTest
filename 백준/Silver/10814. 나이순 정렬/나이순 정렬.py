N = int(input())
members = [[] for _ in range(201)]

for _ in range(N):
    age, name = input().split()
    age = int(age)
    members[age].append((age, name))

for i in range(201):
    for member in members[i]:
        print(member[0], member[1])
