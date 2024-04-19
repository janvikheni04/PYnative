#Concatenate two data frames using the following conditions
import pandas as pd
a = pd.read_csv("C:\\Users\\admin\\Desktop\\Pynative\\Pandas\\Automobile_data.csv")

GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
a = pd.DataFrame.from_dict(GermanCars)

japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}
a1 = pd.DataFrame.from_dict(japaneseCars)

a3 = pd.concat([a, a1], keys=["Germany", "Japan"])
print(a3)

