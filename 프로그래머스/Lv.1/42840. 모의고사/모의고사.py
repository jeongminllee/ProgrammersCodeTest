def solution(answers):
    answer = [0, 0, 0]
    ans1 = [1, 2, 3, 4, 5]
    ans2 = [2, 1, 2, 3, 2, 4, 2, 5]
    ans3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    result = []
    for idx, val in enumerate(answers):
        if ans1[idx % len(ans1)] == val:
            answer[0] += 1
        if ans2[idx % len(ans2)] == val:
            answer[1] += 1
        if ans3[idx % len(ans3)] == val:
            answer[2] += 1

    for i in range(len(answer)):
        if answer[i] == max(answer):
            result.append(i + 1)

    return sorted(result)