dct = {'S':0, 'D':1, 'H':2, 'C':3}

T = int(input())
for test_case in range(1, T+1) :
    st = input()
    arr = [[] for _ in range(4)]

    # [1] 리스트에 추가
    for i in range(0, len(st), 3) :
        arr[dct[st[i]]].append(int(st[i+1:i+3]))

    ans = []
    for lst in arr :
        if len(lst) != len(set(lst)) :  # 오류
            print(f"#{test_case} ERROR")
            break

        ans.append(13-len(lst))

    else :
        print(f"#{test_case}", *ans)