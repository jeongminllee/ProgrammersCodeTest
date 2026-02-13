def main() :
    N = int(input())
    H = list(map(int, input().split()))
    tour = {}
    res = 0

    for idx, height in enumerate(H):
        if 0 < idx < (N - 1) :
            if H[idx - 1] < height and H[idx + 1] < height :
                res += 1

    return res

if __name__ == "__main__" :
    T = int(input())
    for test_case in range(1,T+1) :
        print(f"Case #{test_case}: {main()}")