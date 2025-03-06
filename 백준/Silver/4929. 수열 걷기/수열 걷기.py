import sys
input = sys.stdin.readline

from bisect import bisect_left, bisect_right
def sol_4929() :
    while True :
        lst1 = list(map(int, input().split()))
        if sum(lst1) == 0 :
            break
        n = lst1[0]
        sequence1 = lst1[1:]
        lst2 = list(map(int, input().split()))
        m = lst2[0]
        sequence2 = lst2[1:]

        ans = 0
        idx1 = 0    # 수열 1의 동일한 숫자의 index
        idx2 = 0    # 수열 2의 동일한 숫자의 index

        for num in sequence1 :
            # 동일한 숫자가 있으면
            if bisect_right(sequence2, num) - bisect_left(sequence2, num) > 0 :
                # 첫 번째 수열의 해당 숫자까지의 합
                sum_seq1 = sum(sequence1[idx1:bisect_right(sequence1, num)])
                # 두 번째 수열의 해당 숫자까지의 합
                sum_seq2 = sum(sequence2[idx2:bisect_right(sequence2, num)])

                # 각 수열의 누적합 중 큰 값을 ans에 누적
                ans += max(sum_seq1, sum_seq2)

                # 각 수열의 index 갱신
                idx1 = bisect_right(sequence1, num)
                idx2 = bisect_right(sequence2, num)

        # 마지막 길의 최댓값을 구해 ans에 추가
        ans += max(sum(sequence1[idx1:]), sum(sequence2[idx2:]))
        print(ans)

sol_4929()