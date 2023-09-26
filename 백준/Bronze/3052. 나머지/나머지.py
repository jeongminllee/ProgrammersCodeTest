arr = []
for i in range(10) :
    num = int(input())
    if num % 42 not in arr :
        arr.append(num % 42)

print(len(arr))


# arr = []
# for i in range(10):
#     a = int(input())
#     arr.append(a % 42)
# print(len(set(arr)))
