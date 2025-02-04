from typing import List, Tuple

def solve(W: int, H: int, A: int) -> int:
    if W * H < A:
        return -1
    
    # 원본 W, H 저장
    ori_W, ori_H = W, H
    
    # A의 약수 쌍을 저장할 리스트
    fold: List[Tuple[int, int]] = []
    
    # A가 1인 경우 처리
    if A == 1:
        fold.append((1, 1))
    
    # A의 약수 쌍 찾기
    for i in range(1, A // 2 + 1):
        if A % i == 0:
            fold.append((i, A // i))
    
    # W, H를 반으로 접었을 때의 값들을 저장
    width: List[int] = []
    height: List[int] = []
    
    # W를 반으로 접는 과정
    temp_W = W
    while temp_W != 1:
        temp_W = (temp_W + 1) // 2
        width.append(temp_W)
    
    # H를 반으로 접는 과정
    temp_H = H
    while temp_H != 1:
        temp_H = (temp_H + 1) // 2
        height.append(temp_H)
    
    # 정렬
    width.sort()
    height.sort()
    
    # 최소값 초기화
    mn = float('inf')
    
    # 모든 약수 쌍에 대해 검사
    for w, h in fold:
        # 첫 번째 경우: w가 가로, h가 세로
        if ori_W >= w and ori_H >= h:
            fold_w = fold_h = 0
            
            if w != ori_W:
                # width 리스트에서 w+1 이상인 값들의 개수 + 1
                idx = len([x for x in width if x < w + 1])
                fold_w = len(width) - idx + 1
            
            if h != ori_H:
                # height 리스트에서 h+1 이상인 값들의 개수 + 1
                idx = len([x for x in height if x < h + 1])
                fold_h = len(height) - idx + 1
            
            mn = min(mn, fold_w + fold_h)
        
        # 두 번째 경우: h가 가로, w가 세로 (회전한 경우)
        if ori_W >= h and ori_H >= w:
            fold_w = fold_h = 0
            
            if h != ori_W:
                idx = len([x for x in width if x < h + 1])
                fold_w = len(width) - idx + 1
            
            if w != ori_H:
                idx = len([x for x in height if x < w + 1])
                fold_h = len(height) - idx + 1
            
            mn = min(mn, fold_w + fold_h)
    
    return -1 if mn == float('inf') else mn

# 입력 받기
W, H, A = map(int, input().split())

# 결과 출력
print(solve(W, H, A))