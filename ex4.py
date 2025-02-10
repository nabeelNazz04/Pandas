import pandas as pd
df=pd.read_csv("movies_data.csv")
print(df)
g=df.groupby('industry')
print('Size:',g.size())
print(g.get_group("Bollywood"))



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
#groupby based on the grouper function and store it in a variable 'g'
#Note: use the imdb_rating column
g=df.groupby(lambda idx:grouper(df,idx,'imdb_rating'))

#iterate through the 'g' and print all the groups
for key,data in g:
  print("Key:",key)
  print('Data:',data)