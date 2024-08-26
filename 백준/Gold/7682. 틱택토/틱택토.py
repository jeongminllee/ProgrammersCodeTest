def is_valid(arr, a) :
    for i in range(3) :
        for j in range(3) :
            if (a == arr[0][j] == arr[1][j] == arr[2][j]):    # 세로
                return True
            elif (a == arr[i][0] == arr[i][1] == arr[i][2]):  # 가로
                return True
            elif ((a == arr[0][0] == arr[1][1] == arr[2][2]) or (a == arr[2][0] == arr[1][1] == arr[0][2])) : # 대각
                return True

    return False

while True :
    s = input()
    if s == 'end' :
        break

    arr = [list(s[i:i+3]) for i in range(0, 9, 3)]

    if s.count('X') - s.count('O') > 2 :
        print('invalid')
        continue

    if s.count('X') < s.count('O') :
        print('invalid')
        continue

    if s.count('X') - s.count('O') == 0 and is_valid(arr, 'O') and not is_valid(arr, 'X') :
        print("valid")
        continue

    if s.count('X') - s.count('O') == 1 and is_valid(arr, 'X') and not is_valid(arr, 'O') :
        print("valid")
        continue

    if s.count('.') == 0 and s.count('X') - s.count('O') == 1 and not is_valid(arr, 'O') :
        print("valid")
        continue

    else :
        print('invalid')