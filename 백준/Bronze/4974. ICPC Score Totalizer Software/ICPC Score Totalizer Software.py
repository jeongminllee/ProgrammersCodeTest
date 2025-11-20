def main() :
    while True :
        n = int(input())
        if n == 0 :
            break
        scores = [int(input()) for _ in range(n)]
        scores.sort()
        scores.pop()
        scores.pop(0)

        result = sum(scores) // len(scores)

        print(result)


if __name__ == "__main__" :
    main()