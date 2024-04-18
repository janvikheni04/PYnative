#Convert string into a datetime object
from datetime import datetime
s = "Feb 25 2020 4:20PM"

d_obj = datetime.strptime(s , '%b %d %Y %I:%M%p')
print(d_obj)