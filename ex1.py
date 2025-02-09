import pandas as pd

# 1) Load the CSV file
df = pd.read_csv("movies_data.csv")
print(df.head())
print('***********************************')

# 2) Add the 'year_classify' column based on the 'release_year' column
df['year_classify'] = df['release_year'].apply(lambda x: 'before 2000' if x < 2000 else 'From 2000')
print(df)

# 3) Select only the desired columns
columns_to_include = ['movie_id', 'budget', 'revenue', 'year_classify']
df_selected = df[columns_to_include]

# 4) Save the updated DataFrame with selected columns to a new CSV file
output_file = 'final_movie_data.csv'
df_selected.to_csv(output_file, index=False)  # Ensure index=False to exclude the index column

# 5) Verify the saved file by reading it back
df_final = pd.read_csv(output_file)
print(df_final)