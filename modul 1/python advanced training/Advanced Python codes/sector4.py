import datetime

varb = datetime.datetime(1905, 6, 23)

print(type(varb))

print(varb.year)
print(varb.month)
print(varb.day)
getattr(varb,'year')