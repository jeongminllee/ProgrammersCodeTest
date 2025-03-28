def sol_11269() :
    words = input().rstrip()
    words.upper()
    cnt = 0
    for i in range(len(words)) :
        if i % 3 == 0 and words[i] != 'P' :
            cnt += 1
        if i % 3 == 1 and words[i] != 'E' :
            cnt += 1
        if i % 3 == 2 and words[i] != 'R' :
            cnt += 1

    print(cnt)


sol_11269()