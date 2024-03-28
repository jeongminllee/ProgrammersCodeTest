def solution(wallpaper):
    lux, luy, rdx, rdy = 51, 51, 0, 0
    for x in range(len(wallpaper)) :
        for y in range(len(wallpaper[0])) :
            if wallpaper[x][y] == "#" :
                lux = min(lux, x)
                luy = min(luy, y)
                rdx = max(rdx, x + 1)
                rdy = max(rdy, y + 1)
    return [lux, luy, rdx, rdy]