def main() :
    L, N = map(int, input().split())
    dct = {}
    for _ in range(L) :
        fr, to = input().split()
        dct[fr] = to

    res = []
    aeiou = ['a', 'e', 'i', 'o', 'u;']
    for _ in range(N) :
        words = input()
        if words in dct.keys() :
            res.append(dct[words])
        else :
            if words[-2] not in aeiou and words[-1] == 'y' :
                words = words.replace(words[-1], 'ies')
            elif words.endswith('o') or words.endswith('s') or words.endswith('ch') or words.endswith('sh') or words.endswith('x') :
                words += 'es'
            else :
                words += 's'

            res.append(words)

    for r in res :
        print(r)
main()