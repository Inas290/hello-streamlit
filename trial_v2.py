import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

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
    ('Home Page', 'Tourism per Country', 'Tourism per Stay Mode')
)

if user_menu == 'Home Page':
    # Display title, description, and photo for the Home Page
    st.title("Tourism Data Analysis")
    st.write("Tourism is a dynamic and global industry that revolves around the concept of people traveling to various destinations for leisure, adventure, or exploration. It plays a pivotal role in promoting cultural exchange, economic growth, and mutual understanding between nations. Tourists seek diverse experiences, from relaxing on exotic beaches and exploring historical landmarks to immersing themselves in the rich tapestry of different cultures. As a powerful economic driver, tourism generates revenue, creates job opportunities, and sustains local communities. It also encourages environmental conservation and the preservation of heritage sites. In essence, tourism is a vibrant and multifaceted sector that bridges cultures, fosters economic development, and kindles a sense of wonder in travelers worldwide.")
    st.image("https://raw.githubusercontent.com/Inas290/hello-streamlit/main/tour.jpg")

elif user_menu == "Tourism per Country":
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

        # Create a line plot using Plotly Express
        fig = px.line(yearly_data, x=yearly_data.index, y=yearly_data.columns, title=f'{variable} by Year in {selected_country}')
        st.plotly_chart(fig)

elif user_menu == "Tourism per Stay Mode":
    st.title("Grouped Bar Plot for Tourism Data")

    # Specify x as the 'country' column, y as the years, and color as the 'variable' (stay mode)
    x = 'country'
    y = ['2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']
    color = 'variable'

    # Create the grouped bar plot
    fig = px.bar(df, x=x, y=y, color=color,
             labels={'variable': 'Stay Mode'},
             title='Total Spending by Year and Stay Mode in Different Countries')

    # Customize the layout
    fig.update_layout(barmode='group', xaxis_title='Country', yaxis_title='Total Spending')

    # Display the plot in Streamlit
    st.plotly_chart(fig)
