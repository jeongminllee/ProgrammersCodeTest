N = int(input())
courses = []
for _ in range(N) :
    tmp = list(map(int, input().split()))
    courses.append(set(tmp[1:]))

M = int(input())
students = []
for _ in range(M) :
    tmp = list(map(int, input().split()))
    students.append(set(tmp[1:]))

# for student in students :
#     cnt = 0
#     for course in courses :
#         if course.intersection(student) == course :
#             cnt += 1
#     print(cnt)
    
lst = [0] * M
for i in range(M) :
    for j in range(N) :
        cnt = 0
        for t in courses[j] :
            if t in students[i] :
                cnt += 1
        if cnt == len(courses[j]) :
            lst[i] += 1

print(*lst, sep="\n")