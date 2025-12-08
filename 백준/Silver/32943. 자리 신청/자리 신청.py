def main() :
    X, C, K = map(int, input().split())
    logs = [list(map(int, input().split())) for _ in range(K)]
    logs.sort()

    seat = [0] * (C+1)
    students = [0] * (X+1)

    for _, S, N in logs :
        if seat[S] != 0 :
            continue
        elif students[N] != S :
            seat[students[N]] = 0
            students[N] = S
            seat[S] = N
        else :
            seat[S] = N
            students[N] = S

    for student, seat_num in enumerate(students) :
        if student == 0 or seat_num == 0 :
            continue

        print(student, seat_num)

if __name__ == "__main__" :
    main()