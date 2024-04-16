def solution(land):
    land_copy = land.copy()
    for i in range(1, len(land)) :
        for j in range(4) :
            land_copy[i][j] += max(land_copy[i-1][:j] + land_copy[i-1][j+1:])
    return max(land_copy[-1])