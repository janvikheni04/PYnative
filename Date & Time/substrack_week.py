#Subtract a week (7 days)  from a given date in Python
from datetime import datetime, timedelta  

given_date = datetime(2020, 2, 25)
print("Given date:", given_date)

days_w = 7
a1 = given_date - timedelta(days=days_w)
print(a1)
