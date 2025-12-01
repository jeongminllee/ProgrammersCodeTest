def main() :
    N, K = map(int, input().split())
    S = input()

    cnt = 0
    for i in range(N//2) :
        if S[i] != S[N-i-1] :
            cnt += 1

    return abs(K - cnt)

if __name__ == "__main__" :
    T = int(input())
    for t in range(1, T+1) :
        print(f"Case #{t}: {main()}")