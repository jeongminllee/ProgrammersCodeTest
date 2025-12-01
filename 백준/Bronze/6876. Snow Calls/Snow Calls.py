def main() :
    t = int(input())
    for _ in range(t) :
        S = input()
        trans = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "22233344455566677778889999")
        res = S.replace('-', '').translate(trans)[:10]
        print(f"{res[:3]}-{res[3:6]}-{res[6:10]}")

if __name__ == "__main__" :
    main()