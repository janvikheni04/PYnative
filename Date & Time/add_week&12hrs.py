#Add a week (7 days) and 12 hours to a given date
from datetime import datetime, timedelta

given_date = datetime(2020, 3, 22, 10, 00, 00)
print("Given date:", given_date)

day = 7
ad = given_date + timedelta(days=day, hours=12)
print("New date:", ad)