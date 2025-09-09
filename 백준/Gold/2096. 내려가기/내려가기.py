import copy
def main(N, arr) :
    maxDP = copy.deepcopy(arr[0])
    minDP = copy.deepcopy(arr[0])

    for a in arr[1:] :
        maxDP = [a[0] + max(maxDP[0], maxDP[1]), a[1] + max(maxDP), a[2] + max(maxDP[1], maxDP[2])]
        minDP = [a[0] + min(minDP[0], minDP[1]), a[1] + min(minDP), a[2] + min(minDP[1], minDP[2])]

    return max(maxDP), min(minDP)
if __name__ == "__main__" :
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(*main(N,arr))