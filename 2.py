import pandas as pd
df=pd.read_csv("weather_data.csv")
print(df)
df=pd.read_excel("weather_data.xlsx","Sheet1")
print(df)