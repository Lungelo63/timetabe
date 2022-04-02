num =  int(input("Enter a number to be multiplied: "))  #Taking in user input

for i in range (1,13):  #initiating for loop to the range of 1 - 12
    cal = num * i   #user input times range
    print(str(num) + ' ' + 'x' + ' ' + str(i) + ' = ' + str(cal))   #printing out the timetable