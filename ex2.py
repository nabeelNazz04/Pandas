import pandas as pd

# Read the data from the CSV file
df = pd.read_csv("fruits_data.csv")

# Display the shape, columns, and contents of the original DataFrame
print("Original DataFrame:")
print("Shape:", df.shape)
print("Columns:", df.columns)
print(df)
print("-" * 60)

# Fill NaN values with '-1'
print("DataFrame after filling NaN with '-1':")
new_df = df.fillna('-1')
print(new_df)
print("-" * 60)

# Fill NaN values with specific strategies for each column
print("DataFrame after filling NaN with column-specific strategies:")
new_df = df.fillna({
    'apple(1kg)': df['apple(1kg)'].mean(),                 # Fill with mean of 'apple(1kg)'
    'banana(1 dozen)': df['banana(1 dozen)'].mean(),       # Fill with mean of 'banana(1 dozen)'
    'grapes(1kg)': df['grapes(1kg)'].median(),             # Fill with median of 'grapes(1kg)'
    'mango(1kg)': df['mango(1kg)'].median(),               # Fill with median of 'mango(1kg)'
    'Water Melons(1)': "Not Available"                     # Fill with "Not Available"
})
print(new_df)
print("-" * 60)

# Fill NaN values using forward fill method
print("DataFrame after forward fill (method='ffill'):")
new_df = df.fillna(method='ffill')
print(new_df)
print("-" * 60)

# Drop rows with less than 4 non-NaN values
print("DataFrame after dropping rows with less than 4 non-NaN values:")
new_df = df.dropna(thresh=4)
print(new_df)
print("-" * 60)

# Drop rows with any NaN values
print("DataFrame after dropping rows with any NaN values:")
new_df = df.dropna()
print(new_df)
print("-" * 60)

# Save the original DataFrame to a new CSV file
output_file = 'final_data.csv'
df.to_csv(output_file, index=False)

# Read and display the saved CSV file
print("DataFrame from the saved file:")
df = pd.read_csv("final_data.csv")
print(df)
