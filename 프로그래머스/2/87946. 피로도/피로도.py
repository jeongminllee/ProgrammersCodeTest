from itertools import permutations

def solution(k, dungeons) :
    mx = 0
    for i in permutations(dungeons) :
        fatigue = k
        cnt = 0
        for dungeon in i :
            if fatigue >= dungeon[0] :
                fatigue -= dungeon[1]
                cnt += 1

        mx = max(cnt, mx)
    return mx

# def solution(k, dungeons) :
#     mx = 0
#     n = len(dungeons)
#     v = [0] * n
#     order = [0] * n

#     def dfs(d) :
#         nonlocal mx
#         if d == n :
#             fatigue = k
#             cnt = 0
#             for i in order :
#                 if fatigue >= dungeons[i][0] :
#                     fatigue -= dungeons[i][1]
#                     cnt += 1
#             mx = max(cnt, mx)

#         else :
#             for i in range(n) :
#                 if not v[i] :
#                     v[i] = 1
#                     order[d] = i
#                     dfs(d + 1)
#                     v[i] = 0

#     dfs(0)
#     return mx