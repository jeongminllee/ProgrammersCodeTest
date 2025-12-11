def main() :
    n, P, Q = map(int, input().split()) # the number of eggs,
    eggs = list(map(int, input().split()))
    eggs.sort()

    bags = []
    for egg in eggs :
        if len(bags) < P and Q - sum(bags) >= egg :
            bags.append(egg)

    return len(bags)


T = int(input())
for test_cases in range(1, T+1) :
    print(f"Case {test_cases}: {main()}")