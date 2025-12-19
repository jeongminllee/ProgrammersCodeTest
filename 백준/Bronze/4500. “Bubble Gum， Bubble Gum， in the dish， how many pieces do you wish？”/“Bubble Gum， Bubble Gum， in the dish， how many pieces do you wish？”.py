T = int(input())
for _ in range(T) :
    people = list(input().split())
    names = input()
    n = int(input())
    n -= 1

    start = people.index(names)
    res = (start + n) % len(people)
    print(people[res])