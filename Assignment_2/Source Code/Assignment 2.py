########################################################################
##
## CS 101 Lab
## Program #2
## Clay Abner
## Clavyv@umsystem.edu
##
## PROBLEM : Ask user what their grades are, return their weighted grade and letter grade, account
##           for values out of range.
##
## 
## ERROR HANDLING:
##      Make sure varaiables are changed to integers. 
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################




name = input("What is your name?: ")
Labs = int(input("What is your Labs grade?: "))
if Labs > 100:
    Labs = 100
    print("The value has been changed to 100")
elif Labs < 0:
    print("The value has been changed to 0")
    Labs = 0
Exams = int(input("What is your Exams grade?: "))
if Exams >100:
    print("The value has been changed to 100")
    Exams = 100
elif Exams <0:
    print("The value has been changed to 0")
    Exams = 0
Attendance = int(input("What is your Attendance grade?: "))
if Attendance > 100:
    print("The value has been changed to 100")
    Attendance = 100
elif Attendance <0:
    print("The value has been changed to 0")
    Attendance = 0
Weight = Labs*.7 + Exams*.2 + Attendance*.1
print(Weight)
if int(Weight) in range(90,100):
    print(name, "'s grade is an A")
elif int(Weight) in range(80,89):
    print(name, "'s grade is a B")
elif int(Weight) in range(70,79):
    print(name, "'s grade is a C")
elif int(Weight) in range(60,69):
    print(name, "'s grade is a D")
elif int(Weight) in range(0,59):
    print(name, "'s grade is an F")
