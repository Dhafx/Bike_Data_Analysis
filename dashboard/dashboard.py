import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

sns.set(style='dark')
hour_dt = pd.read_csv("https://raw.githubusercontent.com/Dhafx/Bike_data/main/data/hour.csv")
hour_dt.head()
# Calculate average hourly rentals by season
season_avg = hour_dt.groupby("season")["total_count"].mean()

# Set a title for the Streamlit app
st.title("Average Hourly Bike Rentals by Season")

# Display the data as a bar chart
st.bar_chart(season_avg, use_container_width=True, color="pink")  # Use st.bar_chart instead of plotting manually

# Display data as a table (optional)
if st.checkbox("Show Data Table"):
    st.write(season_avg.to_frame().reset_index())

st.write("**Note:** This dashboard visualizes average hourly bike rentals by season based on the provided data.")