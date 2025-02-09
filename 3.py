import pandas as pd

# Load the Excel file
def load_excel_data(file_path):
    """
    Load data from an Excel file into a dictionary of DataFrames.

    Parameters:
    file_path (str): Path to the Excel file.

    Returns:
    dict: A dictionary where keys are sheet names and values are DataFrames.
    """
    try:
        # Read all sheets into a dictionary of DataFrames
        sheets_dict = pd.read_excel("movies_db", sheet_name=None)
        print("Data loaded successfully!")
        return sheets_dict
    except FileNotFoundError:
        print(f"movies_db' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Perform some Pandas operations on the data
def analyze_movies_data(sheets_dict):
    """
    Perform some basic analysis on the movies data.

    Parameters:
    sheets_dict (dict): Dictionary of DataFrames containing the movies data.
    """
    if sheets_dict is None:
        return

    # Access the 'movies' sheet
    movies_df = sheets_dict.get('movies')
    if movies_df is None:
        print("Error: 'movies' sheet not found.")
        return

    # Display the first 5 rows of the 'movies' DataFrame
    print("\nFirst 5 rows of the 'movies' DataFrame:")
    print(movies_df.head())

    # Display basic information about the 'movies' DataFrame
    print("\n'movies' DataFrame Info:")
    print(movies_df.info())

    # Display statistical summary of numeric columns in 'movies'
    print("\nStatistical Summary of 'movies':")
    print(movies_df.describe())

    # Filter movies with an IMDb rating greater than 8.5
    high_rated_movies = movies_df[movies_df['imdb_rating'] > 8.5]
    print("\nHigh-Rated Movies (IMDb Rating > 8.5):")
    print(high_rated_movies)

    # Group movies by industry and count the number of movies in each industry
    industry_counts = movies_df['industry'].value_counts()
    print("\nNumber of Movies by Industry:")
    print(industry_counts)

    # Find the average IMDb rating for each industry
    avg_rating_by_industry = movies_df.groupby('industry')['imdb_rating'].mean()
    print("\nAverage IMDb Rating by Industry:")
    print(avg_rating_by_industry)

    # Sort movies by release year in ascending order
    sorted_by_year = movies_df.sort_values(by='release_year')
    print("\nMovies Sorted by Release Year:")
    print(sorted_by_year)

    # Access the 'financials' sheet
    financials_df = sheets_dict.get('financials')
    if financials_df is None:
        print("Error: 'financials' sheet not found.")
        return

    # Merge 'movies' and 'financials' DataFrames on 'movie_id'
    merged_df = pd.merge(movies_df, financials_df, on='movie_id', how='inner')
    print("\nMerged DataFrame (Movies + Financials):")
    print(merged_df.head())

    # Calculate the profit for each movie
    merged_df['profit'] = merged_df['revenue'] - merged_df['budget']
    print("\nMovies with Profit Calculation:")
    print(merged_df[['title', 'budget', 'revenue', 'profit']].head())

    # Access