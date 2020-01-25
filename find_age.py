import datetime
i = datetime.datetime.now()


print("FIND YOUR AGE EASILY, WITH THIS LITTLE PROGRAM")
print("************************************************")


# user inputs birthday
year = int(input("Enter your birth year   : "))
if len(str(year)) != 4:
    print("You should enter the year in 4 digits")
month = int(input("Enter your birth month  : "))
if month >= 13:
    print("Please check the month again")
date = int(input("Enter your birth date   : "))
if date >= 32:
    print("Please check the date again")
print("------------------------------------------------")


# calculate days
if i.day >= date:
    dd = i.day-date
    new_month = i.month
else:
    dd = (i.day+30)-date
    new_month = i.month-1


# calculate months
if new_month >= month:
    mm = new_month-month
    new_year = i.year

else:
    mm = (new_month+12)-month
    new_year = i.year-1


# calculate years
if new_year >= year and year >= 1000 and month <= 12 and date <= 31:
    yy = new_year-year
    print("You are now " + str(yy) + " year(s), " +
          str(mm) + " month(s) and " + str(dd) + " day(s) old")
    print("------------------------------------------------")
    if len(str(year)) != 4 or month >= 13 or date >= 32:
        print("Probably the output is wrong")
        print("------------------------------------------------")

else:
    yy = new_year-year
    # prints this if current year is smaller than the birth year
    print("Wait, check your inputs again")
    print("------------------------------------------------")
