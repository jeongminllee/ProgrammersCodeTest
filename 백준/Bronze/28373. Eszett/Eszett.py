S = input()
S = S.lower()
print(S)
for i in range(len(S)-1) :
    char = S[i:i+2]
    if char == "ss" :
        print(S[:i] + "B" + S[i+2:])