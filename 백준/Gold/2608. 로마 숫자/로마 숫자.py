rome = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000,
    "IV" : 4,
    "IX" : 9,
    "XL" : 40,
    "XC" : 90,
    "CD" : 400,
    "CM" : 900
}

r_num1 = list(input())
r_num2 = list(input())
nums = 0
r_nums = ''

for i in range(len(r_num1)-1) :
    if r_num1[i] == "I" and (r_num1[i+1] == "V" or  r_num1[i+1] == "X"):
        nums -= 2

    if r_num1[i] == "X" and (r_num1[i+1] == "L" or r_num1[i+1] == "C"):
        nums -= 20

    if r_num1[i] == "C" and (r_num1[i + 1] == "D" or r_num1[i + 1] == "M"):
        nums -= 200

for i in range(len(r_num1)) :
    nums += rome[r_num1[i]]

for i in range(len(r_num2)-1) :
    if r_num2[i] == "I" and (r_num2[i+1] == "V" or  r_num2[i+1] == "X"):
        nums -= 2

    if r_num2[i] == "X" and (r_num2[i+1] == "L" or r_num2[i+1] == "C"):
        nums -= 20

    if r_num2[i] == "C" and (r_num2[i + 1] == "D" or r_num2[i + 1] == "M"):
        nums -= 200

for i in range(len(r_num2)) :
    nums += rome[r_num2[i]]
    
print(nums)
while nums > 0 :
    if nums >= 1000 :
        r_nums += "M"
        nums -= 1000
    elif nums >= 900 :
        r_nums += "CM"
        nums -= 900
    elif nums >= 500 :
        r_nums += "D"
        nums -= 500
    elif nums >= 400 :
        r_nums += "CD"
        nums -= 400
    elif nums >= 100 :
        r_nums += "C"
        nums -= 100
    elif nums >= 90 :
        r_nums += "XC"
        nums -= 90
    elif nums >= 50 :
        r_nums += "L"
        nums -= 50
    elif nums >= 40 :
        r_nums += "XL"
        nums -= 40
    elif nums >= 10 :
        r_nums += "X"
        nums -= 10
    elif nums >= 9 :
        r_nums += "IX"
        nums -= 9
    elif nums >= 5 :
        r_nums += "V"
        nums -= 5
    elif nums >= 4 :
        r_nums += "IV"
        nums -= 4
    elif nums >= 1 :
        r_nums += "I"
        nums -= 1

print(r_nums)