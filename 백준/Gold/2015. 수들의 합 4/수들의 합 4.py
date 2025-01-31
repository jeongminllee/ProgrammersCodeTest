def main() :
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    curr = 0
    cnt = 0

    hashMap = {0 : 1}
    for num in arr :
        curr += num

        if curr - K in hashMap :
            cnt += hashMap[curr - K]

        hashMap[curr] = hashMap.get(curr, 0) + 1

    print(cnt)
main()