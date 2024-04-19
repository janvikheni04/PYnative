#Find the average mileage of each car making company
import pandas as pd
a = pd.read_csv("C:\\Users\\admin\\Desktop\\Pynative\\Pandas\\Automobile_data.csv")

m = a.groupby('company')
m1 = m['company', 'average-mileage'].mean()
print(m1)