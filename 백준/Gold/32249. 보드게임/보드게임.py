import sys
input = sys.stdin.readline

def sol_32249() :
    N, M = map(int, input().split())
    Alice = [list(input().rstrip()) for _ in range(N)]
    Bob = [list(input().rstrip()) for _ in range(N)]

    alice_bottom_b_cnt = Alice[-1].count('B')
    bob_bottom_a_cnt = Bob[-1].count('A')
    print('Alice' if alice_bottom_b_cnt > 0 or bob_bottom_a_cnt == 0 else 'Bob')

    q = int(input())
    for _ in range(q) :
        r1, c1, r2, c2 = [int(x) - 1 for x in input().split()]
        alice_card, bob_card = Alice[r1][c1], Bob[r2][c2]
        if alice_card != bob_card :
            diff = 1 if alice_card == 'A' else -1
            if r1 == N - 1 :
                alice_bottom_b_cnt += diff
            if r2 == N - 1 :
                bob_bottom_a_cnt += diff

        Alice[r1][c1], Bob[r2][c2] = bob_card, alice_card

        print('Alice' if alice_bottom_b_cnt > 0 or bob_bottom_a_cnt == 0 else 'Bob')

sol_32249()