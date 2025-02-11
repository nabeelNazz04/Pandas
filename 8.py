# Usage of matplotlib and seaborn
import pandas as pd

# Read the Excel file
df = pd.read_excel("linechart.xlsx")
print(df)

# Import matplotlib
from matplotlib import pyplot as plt

# Line Plot
plt.figure(figsize=(12, 4))
plt.plot(df["Quarter"], df["Fridge"], color="red", label="Fridge")
plt.plot(df["Quarter"], df["Dishwasher"], color="blue", label="Dishwasher")
plt.plot(df["Quarter"], df["Washing Machine"], color='green', label="Washing Machine")
plt.title("Product Sales")
plt.ylabel("Revenue (min $)")
plt.xlabel("Financial Quarter")
plt.legend()  # Show labels on the top right
plt.show()

# Pie Chart
total_sales = df[["Fridge", "Dishwasher", "Washing Machine"]].sum()
print(total_sales)
print(total_sales.index)
plt.figure(figsize=(6, 6))  # Set figure size for the pie chart
plt.pie(total_sales, labels=total_sales.index, autopct='%1.1f%%',explode=[0.1,0,0],shadow=True,startangle=120, colors=['red', 'blue', 'green'])
plt.title("Total Sales Distribution")
plt.show()
df.plot(kind='bar',x='Quarter')
plt.xticks(rotation=45)
plt.show()
df.set_index("Quarter")
print(df)