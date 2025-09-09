def main(N, M, num_set, num_list) :
    for num in num_list :
        if num in num_set :
            print(1)
        else :
            print(0)

    return

if __name__ == "__main__" :
    N = int(input())
    num_set = set(map(int, input().split()))
    M = int(input())
    num_list = list(map(int, input().split()))
    main(N, M, num_set, num_list)