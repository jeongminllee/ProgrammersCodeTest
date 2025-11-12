def main() :
    N, M = input().split()
    cnt_1 = cnt_0 = 0

    for i in range(len(N)) :
        if N[i] != M[i] :
            if M[i] == '1' :
                cnt_1 += 1
            else :
                cnt_0 += 1

    print(max(cnt_1, cnt_0))
    
T = int(input())
for _ in range(T) :
    main()