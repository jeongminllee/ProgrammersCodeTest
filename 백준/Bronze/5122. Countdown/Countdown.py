def product(lst) :
    res = 1
    for num in lst :
        res *= num
    return res

K = int(input())
for k in range(1, K+1) :
    MLC = list(map(int, input().split()))   # 20, 20, 20, 18, 20 진법
    JDN = int(input())                      #

    end_G_to_J = 2456054
    max_MLC = 13 * 20 * 20 * 18 * 20
    MLC_val = [20, 20, 18, 20, 1]
    D_event = 0
    for i in range(5) :
        D_event += MLC[i] * product(MLC_val[i:])

    end_jdn = JDN + (max_MLC - D_event)
    res = end_jdn - end_G_to_J

    print(f"Data Set {k}:")
    if res > 0 :
        print(res)
    elif res == 0 :
        print("Panic!")
    else :
        print("It's a hoax!")
    print()