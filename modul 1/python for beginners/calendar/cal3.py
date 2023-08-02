import calendar

while True:
    Varyear = int(input("Enter a year after 2000: "))

    if Varyear > 2000:
        Varmonth = int(input("Enter a month (1 to 12): "))
        if 1 <= Varmonth <= 12:
            print(calendar.month(Varyear, Varmonth))
            break
        else:
            print("Enter a valid month (1 to 12)!")
    else:
        print("Enter a proper year after 2000!")

