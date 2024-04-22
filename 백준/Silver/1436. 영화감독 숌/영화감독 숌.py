n = int(input())
cnt = 0         # 현재까지 발견된 종말의 수의 개수
movie_title = 666    # 최초의 종말의 수

while True :
    # 현재 숫자(movie_title)에 '666'이 포함되어 있는지 확인
    if '666' in str(movie_title) :
        cnt += 1    # '666' 이 포함되어 있으면, cnt += 1
    if cnt == n :   # n번째 종말의 수를 찾은 경우
        break       # 반복문 종료
    movie_title += 1    # 다음 숫자로 이동
    
print(movie_title)  # 해당 숫자 출력