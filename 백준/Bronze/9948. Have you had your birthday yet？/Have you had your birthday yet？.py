birthdays = []
while True :
    cmd = input()
    if cmd == '0 #' :
        break
    birthdays.append(cmd)

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
DAY = '4'
MONTH = 'August'
for birthday in birthdays :
    day, month = birthday.split()

    # 2007년은 윤년이 아니므로 패스
    if month == 'February' and day == '29' :
        print('Unlucky')

    elif day == DAY and month == MONTH :
        print('Happy birthday')

    elif months.index(MONTH) > months.index(month) or (months.index(MONTH) == months.index(month) and int(day) < int(DAY)) :
        print("Yes")

    else :
        print('No')