# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")
duration=netflix_df['duration'].mode()[0]
short_movie_count = netflix_df[
    (netflix_df['duration'] < 90) & 
    (netflix_df['genre'] == 'Action') & 
    (netflix_df['release_year'] >= 1990) & 
    (netflix_df['release_year'] < 2000)
].shape[0]

print(short_movie_count)
