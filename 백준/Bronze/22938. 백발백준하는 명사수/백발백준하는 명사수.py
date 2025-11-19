def main() :
    x1, y1, r1 = map(int, input().split())
    x2, y2, r2 = map(int, input().split())

    point_distances = (x1 - x2) ** 2 + (y1 - y2) ** 2
    point_distances = point_distances ** (1/2)
    if point_distances >= r1 + r2 :
        print("NO")
    else :
        print("YES")


if __name__ == "__main__" :
    main()