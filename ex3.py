import pandas as pd

# Load the dataset from the CSV file
df = pd.read_csv("food_db.csv")

# Print the number of rows and columns in the dataset
print('Number of rows and columns:', df.shape)

# Display the entire DataFrame
print(df)

# Replace '5%' and '10%' with '13%' in the entire DataFrame
new_df = df.replace(['5%', '10%'], '13%')

# Display the updated DataFrame after replacement
print(new_df)

# Replace categorical values with numerical values in the entire DataFrame
new_df = df.replace({
    'Excellent': 4,
    'Very Good': 3,
    'Good': 2,
    'Average': 1
})

# Display the updated DataFrame after replacement
print(new_df)