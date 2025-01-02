def minimum_visible_sum(N, dice) :
    ans = 0
    min_list = []

    if N == 1 :
        ans = sum(dice) - max(dice)

    else :
        for i in range(3) :
            min_list.append(min(dice[i], dice[5-i]))
        min_list.sort()

        min_one_face = min_list[0]
        min_two_face = min_list[0] + min_list[1]
        min_three_face = sum(min_list)

        one_face_count = (N - 2) * (N - 2) + 4 * (N - 2) * (N - 1)
        two_face_count = 4 * (N - 1) + 4 * (N - 2)
        three_face_count = 4

        ans = (
            min_one_face * one_face_count +
            min_two_face * two_face_count +
            min_three_face * three_face_count
        )

    return ans

N = int(input())
dice = list(map(int, input().split()))

print(minimum_visible_sum(N, dice))