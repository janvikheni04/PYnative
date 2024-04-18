#Calculate number of days between two given dates
from datetime import datetime

# 2020-02-25
d1 = datetime(2020, 2, 25).date()
# 2020-09-17
d2 = datetime(2020, 9, 17).date()

d = None
if d1>d2:
    print("date 1 is greater")
    d = d1 - d2

else:
    print("date2 is greater")
    d = d2 - d1
print("difference is", d.days, "days")    