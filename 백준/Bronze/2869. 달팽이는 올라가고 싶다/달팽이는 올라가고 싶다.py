A, B, V = map(int, input().split())

height = (V - A) // (A - B)
if (V - A) % (A - B) == 0 :
    print(height + 1)
else :
    print(height + 2)