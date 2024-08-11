arr = list(map(int, input().split()))
copy_arr = arr.copy()

if arr == sorted(copy_arr) :
    print('ascending')
elif arr == sorted(copy_arr, reverse=True) :
    print('descending')
else :
    print('mixed')