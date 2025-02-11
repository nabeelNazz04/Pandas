import pandas as pd

# DataFrames for India and US weather
india_weather = pd.DataFrame({
    'city': ['mumbai', 'delhi', 'bangalore'],
    'temperature': [32, 45, 30],
    'humidity': [80, 60, 78]
})

us_weather = pd.DataFrame({
    'city': ['los angeles', 'canada', 'new york'],
    'temperature': [40, 34, 35],
    'humidity': [85, 65, 87]
})

# Concatenate DataFrames vertically
df = pd.concat([india_weather, us_weather], ignore_index=True)
print("Concatenated DataFrame (ignore_index=True):")
print(df)

# Concatenate DataFrames with keys
df_with_keys = pd.concat([india_weather, us_weather], keys=['India', 'US'])
print("\nConcatenated DataFrame with keys:")
print(df_with_keys)

# Access data using keys
print("\nAccessing data using keys (India):")
print(df_with_keys.loc['India'])

# Column-wise concatenation
temperature = pd.DataFrame({
    'city': ['mumbai', 'delhi', 'bangalore'],
    'temperature': [32, 45, 30]
})

windspeed = pd.DataFrame({
    'city': ['delhi', 'mumbai'],
    'windspeed': [7, 12]
}, index=[1, 0])

print("\nColumn-wise concatenation:")
print(pd.concat([temperature, windspeed], axis=1))

# Merge DataFrames
print("\nMerged DataFrame (using merge function):")
print(pd.merge(temperature, windspeed, on='city'))
print("using outer:")
print(pd.merge(temperature, windspeed, on='city',how='outer'))