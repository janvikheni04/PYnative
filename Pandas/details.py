#Print All Toyota Cars details

import pandas as pd
a = pd.read_csv("C:\\Users\\admin\\Desktop\\Pynative\\Pandas\\Automobile_data.csv")

a1 = a.groupby('company')
car1 = a1.get_group('toyota')
print(car1)