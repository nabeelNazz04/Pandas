# Import pandas library
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv("weather_data.csv")
print(df)

# Get the number of rows and columns in the DataFrame
rows, columns = df.shape
print("Number of rows:", rows)
print("Number of columns:", columns)

# Display the first row of the DataFrame
print("First row:")
print(df.head(1))

# Display the last row of the DataFrame
print("Last row:")
print(df.tail(1))

# Display rows from index 2 to 4 (inclusive)
print("Rows 2 to 4:")
print(df[2:5])

# Print the column names of the DataFrame
print("Column names:")
print(df.columns)

# Print the 'event' column
print("Event column:")
print(df.event)

# Print the 'event' and 'day' columns
print("Event and Day columns:")
print(df[['event', 'day']])

# Calculate and print the maximum temperature
print("Maximum temperature:", df['temperature'].max())

# Calculate and print the mean temperature
print("Mean temperature:", df['temperature'].mean())

# Calculate and print the minimum temperature
print("Minimum temperature:", df['temperature'].min())

# Generate descriptive statistics for the DataFrame
print("Descriptive statistics:")
print(df.describe())

# Filter rows where temperature is greater than or equal to 32
print("Rows where temperature >= 32:")
print(df[df.temperature >= 32])

# Display the day and temperature for the row with the maximum temperature
print("Day and temperature for maximum temperature:")
print(df[['day', 'temperature']][df.temperature == df['temperature'].max()])

# Set 'day' as the index of the DataFrame
df = df.set_index('day')
print("DataFrame with 'day' as index:")
print(df)

# Access the row with index '1/1/2017'
print("Row for day '1/1/2017':")
print(df.loc['1/1/2017'])

# Reset the index to default integer index
df = df.reset_index()
print("DataFrame after resetting index:")
print(df)

# Set 'event' as the index of the DataFrame
df = df.set_index('event')
print("DataFrame with 'event' as index:")
print(df)

# Access rows where the index is 'Sunny'
print("Rows for event 'Sunny':")
print(df.loc['Sunny'])