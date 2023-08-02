import calendar

Varyear = int(input("Enter a year after 2000: "))
Varmonth = int(input("Enter a month: "))

if Varyear>2000:
    print(calendar.month(Varyear,Varmonth))
else:
    print("Enter proper year!")
