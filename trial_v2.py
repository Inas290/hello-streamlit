import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from a CSV file
df = pd.read_csv("dataset-v2.csv")

# Create a Streamlit app
st.set_page_config(
    page_title="Your App Title",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
)

st.sidebar.title("Navigation")
user_menu = st.sidebar.radio(
    'Select an Option',
    ('Home Page', 'Select Country', 'Create Box Plot')
)

if user_menu == 'Home Page':
    # Display title, description, and photo for the Home Page
    st.title("Title")
    st.write("Write description\nOther description")
    st.image("Media/Name.gif", use_column_width=True)

elif user_menu == "Select Country":
    st.title("Country Data Visualization")
    # Select the countries you want to plot (in this example, all countries)
    countries = df['Country'].unique()
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

elif user_menu == "Create Box Plot":
    st.title("Category Box Plots")
    # Select the variable to study
    variable = st.selectbox("Select a Variable", df['Variable'].unique())

    # Filter the data for the selected variable
    data_variable = df[df['Variable'] == variable]

    # Check if data exists for the selected variable
    if data_variable.empty:
        st.write(f"No data available for {variable}")
    else:
        # Create a box plot
        st.pyplot(plt.figure(figsize=(10, 6))
        sns.boxplot(x='Category', y='Value', data=data_variable)
        plt.title(f'Box Plot of {variable} by Category')
        plt.xticks(rotation=45)
        plt.grid(True)
