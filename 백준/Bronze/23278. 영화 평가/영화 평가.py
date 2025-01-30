def main() :
    N, L, H = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()

    for _ in range(L) :
        lst.pop(0)

    for _ in range(H) :
        lst.pop()

    print(sum(lst) / len(lst))
    
main()