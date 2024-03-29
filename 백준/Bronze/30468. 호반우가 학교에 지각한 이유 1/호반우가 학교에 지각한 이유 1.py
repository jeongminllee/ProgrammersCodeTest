STR, DEX, INT, LUK, N = map(int, input().split())

if sum([STR, DEX, INT, LUK]) > N * 4 :
    print(0)
else :
    print((4 * N) - sum([STR, DEX, INT, LUK]))