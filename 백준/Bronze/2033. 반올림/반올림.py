n = int(input())
n_length = len(str(n))
for _ in range(n_length - 1) :
    if n % 10 >= 5 :
        n //= 10
        n += 1
    elif n % 10 < 5 :
        n //= 10

print(n * (10 ** (n_length - 1)))