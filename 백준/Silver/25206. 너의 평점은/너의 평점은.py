scores = {
    "A+" : 4.5,
    "A0" : 4.0,
    "B+" : 3.5,
    "B0" : 3.0,
    "C+" : 2.5,
    "C0" : 2.0,
    "D+" : 1.5,
    "D0" : 1.0,
    "F" : 0.0
}
calc_gpa = total_gpa = 0

for i in range(20) :
    names, gpa, score = input().split(' ')
    if score == 'P' :
        continue
    calc_gpa += float(gpa) * scores[score]
    total_gpa += float(gpa)

res = calc_gpa / total_gpa
print(res)