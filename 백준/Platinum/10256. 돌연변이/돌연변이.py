def count_marker_occurrences(dna, marker):
    count = 0
    n, m = len(dna), len(marker)

    # 마커의 모든 가능한 돌연변이 생성
    mutations = set()
    for i in range(m + 1):
        for j in range(i, m + 1):
            mutation = marker[:i] + marker[i:j][::-1] + marker[j:]
            mutations.add(mutation)

    # DNA에서 각 돌연변이의 출현 횟수 계산
    for i in range(n - m + 1):
        if dna[i:i + m] in mutations:
            count += 1

    return count


# 테스트 케이스 수 입력
T = int(input())

for _ in range(T):
    # DNA 길이와 마커 길이 입력
    n, m = map(int, input().split())

    # DNA와 마커 입력
    dna = input().strip()
    marker = input().strip()

    # 결과 출력
    result = count_marker_occurrences(dna, marker)
    print(result)