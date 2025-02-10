import pandas as pd
df=pd.read_csv("weather_by_cities.csv")
print(df)
g=df.groupby('city')
for city,data in g:
  print('city:',city)
  print("max:",data.temperature.max())

print(g.get_group("mumbai"))

print(g.max())
#print(g.mean())
print(g.describe())
print(g.size())
def grouper(df,idx,col):
  if 80<= df[col].loc[idx]<=90:
    return '80-90'
  elif 50<=df[col].loc[idx]<=60:
    return '50-60'
  else:
    return 'others'
g=df.groupby(lambda idx:grouper(df,idx,'temperature'))
for key,data in g:
  print("key:",key)
  print("data:",data)
def grouper(df, idx, col):
    '''
        This function returns category based on imdb_ratin
    '''
    if 1<= df[col].loc[idx] <=3.9:
        return 'Poor'
    elif 4<= df[col].loc[idx] <=7.9:
        return 'Average'
    elif 8<= df[col].loc[idx] <=10:
        return 'Good'
    else:
        return 'others'