def main() :
    n = int(input())
    lst = list(input().split())

    res = 0
    for char in lst :
        mid = (len(char) - 1) // 2
        if len(char) % 2 == 0:
            left, right = mid, mid + 1

            while left > 0 and right < len(char) - 1 :
                if char[left] == char[right] :
                    left -= 1
                    right += 1
                else :
                    break

            if left == 0 and right == (len(char) - 1) and char[left] == char[right]:
                res += int(char)

        else :
            left, right = mid, mid

            while left > 0 and right < len(char) - 1:
                if char[left] == char[right]:
                    left -= 1
                    right += 1
                else:
                    break

            if left == 0 and right == (len(char) - 1) and char[left] == char[right]:
                res += int(char)

    print(res)

if __name__ == "__main__" :
    main()
