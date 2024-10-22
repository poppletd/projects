'''
Name: Delaina
Date: 10/22/24
Assignment: Unit 2 and 3 Project
'''

#spring = march 20
#summer = june 21
#fall = september 22
#winter = december 21

user_month = input("Enter the name of the month: ")
month = user_month.title()
day = int(input("Enter the day: "))

if month == "March" and day >= 20 or month == "April" or month == "May" or month == "June" and day < 21:
    print(f"{month} {day} is in Spring")
elif month == "June" and day >= 21 or month == "July" or month == "August" or month == "September" and day < 22:
    print(f"{month} {day} is in Summer")
elif month == "September" and day >= 22 or month == "October" or month == "November" or month == "December" and day < 21:
    print(f"{month} {day} is in Fall")
elif month == "December" and day >= 21 or month == "January" or month == "February" or month == "March" and day < 20:
    print(f"{month} {day} is in Winter")
else:
    print("invalid input")
