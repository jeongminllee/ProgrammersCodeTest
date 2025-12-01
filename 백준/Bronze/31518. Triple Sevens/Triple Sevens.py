def main() :
    n = int(input())
    slot_machine = [list(map(int, input().split())) for _ in range(3)]
    for slot in slot_machine :
        if 7 not in slot :
            print(0)
            return

    print(777)

if __name__ == "__main__" :
    main()