day_of_month = 31,28,31,30,31,30,31,31,30,31,30,31
# month = int(input("plesae the month."))
# print (tuple[month-1])

month = int(input("please input month."))
day = int(input("please input day."))
days = 0
for index in range(month-1):
    days += day_of_month[index]
days += day
print (days)

print (sum(day_of_month[:month-1])+day)