import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from a CSV file
df = pd.read_csv("https://raw.githubusercontent.com/Inas290/hello-streamlit/main/dataset-v2.csv")

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
    st.write("Tourism is a dynamic and global industry that revolves around the concept of people traveling to various destinations for leisure, adventure, or exploration. It plays a pivotal role in promoting cultural exchange, economic growth, and mutual understanding between nations. Tourists seek diverse experiences, from relaxing on exotic beaches and exploring historical landmarks to immersing themselves in the rich tapestry of different cultures. As a powerful economic driver, tourism generates revenue, creates job opportunities, and sustains local communities. It also encourages environmental conservation and the preservation of heritage sites. In essence, tourism is a vibrant and multifaceted sector that bridges cultures, fosters economic development, and kindles a sense of wonder in travelers worldwide.")
    st.image("https://raw.githubusercontent.com/Inas290/hello-streamlit/main/tour.jpg")

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

        # Ensure that the DataFrame is correctly structured
        st.write(yearly_data.head())  # Check the structure of the DataFrame
        
        # Convert string data to numbers (may contain commas)
        yearly_data = yearly_data.apply(lambda x: x.str.replace(',', '').astype(float)

        # Check the structure of the transformed DataFrame
        st.write(yearly_data.head())

        # Transpose the data so that years are on the x-axis
        yearly_data = yearly_data.T

        # Check the structure of the transposed DataFrame
        st.write(yearly_data.head())

        # Set up the plot
        st.pyplot(plt.figure(figsize=(12, 6)))
        plt.plot(yearly_data.index, yearly_data.values, marker='o')
        plt.xlabel('Year')
        plt.ylabel('Value')
        plt.title(f'{variable} by Year in {selected_country}')
        plt.xticks(rotation=45)
        plt.grid(True)

