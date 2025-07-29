def solution(genres, plays):
    # 장르별로 가장 많이 재생된 노래를 두 개씩 모아서 앨범 출시
    # 가장 많이 재생된 장르
    # 장르 내에서 많이 재생된 노래
    # 같은 재생 횟수라면, 낮은 고유 번호
    answer = []
    dct1 = {genre:[] for genre in genres}
    dct2 = {genre:0 for genre in genres}
    
    for i, (genre, play) in enumerate(zip(genres, plays)):
        dct1[genre].append((i, play))
        dct2[genre] = dct2.get(genre, 0) + play
    
    for (k, v) in sorted(dct2.items(), key=lambda x:x[1], reverse=True) :
        for (i, p) in sorted(dct1[k], key=lambda x:x[1], reverse=True)[:2] :
            answer.append(i)
            
    return answer