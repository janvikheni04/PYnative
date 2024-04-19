import pandas as pd
import matplotlib.pyplot as plt  

df = pd.read_csv("C:\\Users\\admin\\Desktop\\Pynative\\MatplotLib\\company_sales_data.csv")

profit = df['total_profit'].tolist()
months = df['month_number'].tolist()

plt.plot(months, profit, label = 'Profit data of last year', color='r', marker='o', markerfacecolor='k', linestyle='--', linewidth=3)

plt.xlabel('Month Number')
plt.ylabel('Profit in dollar')
plt.title('Company Sales data of last year')
plt.legend(loc='lower right')
plt.xticks(months)
plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.show()