# 투포인터

N = int(input())
lst = list(map(int, input().split()))
left, right = 0, N-1

solution = abs(lst[left] + lst[right])
sol_left = left
sol_right = right

while left < right :
    tmp = lst[left] + lst[right]

    if abs(tmp) < solution :
        sol_left = left
        sol_right = right
        solution = abs(tmp)

        if solution == 0 :
            break

    if tmp < 0 :
        left += 1
    else :
        right -= 1

print(lst[sol_left], lst[sol_right])