import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data from a CSV file
df = pd.read_csv("dataset-v2.csv")

# Select the countries you want to plot (in this example, all countries)
countries = df['Country'].unique()

# Create a Streamlit app
st.title("Country Data Visualization")
selected_country = st.selectbox("Select a Country", countries)

# Filter the data for the selected country
data_country = df[df['Country'] == selected_country]

# Check if data exists for the selected country
if data_country.empty:
    st.write(f"No data available for {selected_country}")
else:
    # Extract the variable and yearly data
    variable = data_country['Variable'].values[0]
    yearly_data = data_country.iloc[:, 2:]

    # Convert string data to numbers (may contain commas)
    yearly_data = yearly_data.apply(lambda x: x.str.replace(',', '').astype(float))

    # Transpose the data so that years are on the x-axis
    yearly_data = yearly_data.T

    # Set up the plot
    st.pyplot(plt.figure(figsize=(12, 6)))
    plt.plot(yearly_data.index, yearly_data.values, marker='o')
    plt.xlabel('Year')
    plt.ylabel('Value')
    plt.title(f'{variable} by Year in {selected_country}')
    plt.xticks(rotation=45)
    plt.grid(True)
