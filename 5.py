import pandas as pd
import numpy as np
df=pd.read_csv("weather_data.csv")
print(df)
print(df.replace([-88888,-99999],np.nan))
# Replace coloumn wise
new_df=df.replace({
  'temperature':-99999,
  'windspeed':[-88888,-99999],
  'event':'no event'
},np.nan)
print(new_df)
# Old value to new value replacement

print(df.replace({
  -99999:np.nan,
  -88888:np.nan,
  'no event':'Sunny'
}))