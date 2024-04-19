#Find each company’s Higesht price car
import pandas as pd
a = pd.read_csv("C:\\Users\\admin\\Desktop\\Pynative\\Pandas\\Automobile_data.csv")

c = a.groupby('company')
p = c['company', 'price'].max()
print(p)