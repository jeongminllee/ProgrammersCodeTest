def solution(dots):
    if gradient(dots[0], dots[1]) == gradient(dots[2], dots[3]) :
        return 1
    elif gradient(dots[0], dots[2]) == gradient(dots[1], dots[3]) :
        return 1
    elif gradient(dots[0], dots[3]) == gradient(dots[1], dots[2]) :
        return 1
    return 0

def gradient(d1, d2) :
    return (d2[1] - d1[1]) / (d2[0] - d1[0])