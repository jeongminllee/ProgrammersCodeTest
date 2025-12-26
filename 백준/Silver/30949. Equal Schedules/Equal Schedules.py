from collections import defaultdict
schedules = [[] for _ in range(2)]
d = 0
while True :
    try :
        schedule = input()
        if schedule == "======" :
            break
        if schedule == "------" :
            d = 1
            continue

        schedules[d].append(schedule)

    except :
        break

first = defaultdict(int)
second = defaultdict(int)
for i in range(2) :
    for sche in schedules[i] :
        s, e, name = sche.split()
        if i == 0 :
            first[name] += int(e) - int(s)
        else :
            second[name] += int(e) - int(s)

res = defaultdict(int)
diff_val = 0

for idx, val in first.items() :
    if idx not in second :
        res[idx] = -val
        diff_val += abs(val)

    else :
        res[idx] = second[idx] - val
        diff_val += abs(second[idx] - val)

for idx, val in second.items() :
    if idx not in first :
        res[idx] = val
        diff_val += abs(val)

ans = list(res.items())
ans.sort()

for a in ans :
    if diff_val == 0 :
        print("No differences found.")
        break

    if a[1] == 0 :
        continue
    elif a[1] > 0 :
        print(f"{a[0]} +{a[1]}")
    else :
        print(f"{a[0]} {a[1]}")