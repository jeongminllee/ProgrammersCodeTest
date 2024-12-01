# 직각 삼각형을 구합시다.
# 피타고라스 정리를 활용하여 가장 긴 변을 뒤로 보내고
# A ^ 2 + B ^ 2 == C ^ 2 가 맞으면 right, 틀리면 wrong

while True :
    triangle = list(map(int, input().split()))
    if triangle == [0,0,0] :
        break

    triangle.sort()

    if triangle[0] ** 2 + triangle[1] ** 2 == triangle[2] ** 2 :
        print('right')
    else :
        print('wrong')