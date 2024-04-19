#Read Total profit of all months and show it using a line plot
import pandas as pd
import matplotlib.pyplot as plt  

df = pd.read_csv("C:\\Users\\admin\\Desktop\\Pynative\\MatplotLib\\company_sales_data.csv")
print(df)

profit = df['total_profit'].tolist()
months = df['month_number'].tolist()

plt.plot(months, profit)
plt.xlabel('Month number')
plt.ylabel('Profit imn dollar')
plt.xticks(months)
plt.title("Profit per month")
plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.show()