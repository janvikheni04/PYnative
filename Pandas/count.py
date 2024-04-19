#Count total cars per company

import pandas as pd
a = pd.read_csv("C:\\Users\\admin\\Desktop\\Pynative\\Pandas\\Automobile_data.csv")

print(a['company'].value_counts())