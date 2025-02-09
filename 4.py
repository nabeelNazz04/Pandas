import pandas as pd
df=pd.read_csv("weather_data.csv")
print(df)
#to set string day as integer date
df=pd.read_csv("weather_data.csv",parse_dates=['day'])
print(df)
df=df.set_index('day')
print(df)
#df.fillna(0,inplace=True)will fill na values with 0
df.fillna({
  'temperature':df.temperature.mean(),
  'windspeed':df.windspeed.mean(),
  'event':'No event'
})
print(df)
#forward fill using ffill
print(df.fillna(method='ffill'))
#alseo ther is backward fill method
print(df.fillna(method='bfill'))
#coloumn order backfill
print(df)
print(df.fillna(method='bfill',axis='columns'))
#Equal incrementation using linear interpolation method
print(df.interpolate())

# dropna
print(df)
print(df.dropna())
print(df.dropna(how='all'))
print(df.dropna(thresh=2))#drop if there is two na value