#Sort all cars by Price column
import pandas as pd
a = pd.read_csv("C:\\Users\\admin\\Desktop\\Pynative\\Pandas\\Automobile_data.csv")

a = a.sort_values(by=['price', 'horsepower'],ascending=False )
print(a)