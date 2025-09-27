def checknumber(num,num2):
    if num > num2:
        print(num, "is bigger than " , num2)
        return num
    if num == num2:
        print("The numbers are equal to each other")
        return num
    print(num2 , "is bigger than ", num)
    return num2
num = 1
num2 = 1
value = checknumber(num,num2)
print(value)