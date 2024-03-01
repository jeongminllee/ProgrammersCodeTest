def solution(sizes) :
    w = []
    h = []
    for i, j in sizes :
        w.append(max(i, j))
        h.append(min(i, j))
    return max(w) * max(h)