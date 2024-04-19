#Find the most expensive car company name
import pandas as pd

a = pd.read_csv("C:\\Users\\admin\\Desktop\\Pynative\\Pandas\\Automobile_data.csv")
a = a[['company', 'price']][a.price==a['price'].max()]
print(a)