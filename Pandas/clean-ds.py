#Clean the dataset and update the CSV file

import pandas as pd
import pandas as pd
a = pd.read_csv("C:\\Users\\admin\\Desktop\\Pynative\\Pandas\\Automobile_data.csv", na_values={

'price':["?","n.a"],
'stroke':["?","n.a"],
'horsepower':["?","n.a"],
'peak-rpm':["?","n.a"],
'average-mileage':["?","n.a"]})



a.to_csv("C:\\Users\\admin\\Desktop\\Pynative\\Pandas\\Automobile_data.csv")


