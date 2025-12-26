from collections import defaultdict

schedules = defaultdict(int)
while True :
    try :
        x, y, z = input().split()
    except :
        break
    schedules[z] += -(int(y) - int(x))
while True:
    try:
        x, y, z = input().split()
    except:
        break
    schedules[z] += (int(y) - int(x))

res = [name for name in sorted(schedules) if schedules[name]]

if res :
    for name in res :
        print(name, schedules[name]\
            if schedules[name] < 0 else '+' + str(schedules[name]))
else :
    print("No differences found.")