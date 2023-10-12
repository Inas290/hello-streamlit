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
    #st.title("Category Box Plots")
    # Select the variable to study
    #variable = st.selectbox("Select a Variable", df['Variable'].unique())

    # Filter the data for the selected variable
    #data_variable = df[df['Variable'] == variable]

    # Check if data exists for the selected variable
    #if data_variable.empty:
    #    st.write(f"No data available for {variable}")
    #else:
        # Create a notched horizontal box plot using Plotly Express
     #   fig = px.box(data_variable, x='Value', y='Category', color='Category', title=f'Box Plot of {variable} by Category')
      #  st.plotly_chart(fig)
    
    
    #st.title("Notched Horizontal Box Plot")
    
    # Create a notched horizontal box plot using Plotly Express
    #fig = px.box(df, x='2021', y='Country', color='Variable', notched=True,
    #             category_orders={"variable": ["Total domestic trips", "Overnight visitors (tourists)"]},
    #             title="Notched Horizontal Box Plot: Money Spent in 2021 by Tourists in eavh Country (Colored by Variable)")
    
    # Display the plot using st.plotly_chart
    #st.plotly_chart(fig)


    elif user_menu == "Tourism per Stay Mode":
    st.title("Notched Horizontal Box Plot")
    
    # Create a notched horizontal box plot using Plotly Express
    fig = px.box(df.melt(id_vars=['Country', 'Variable'], var_name='Year', value_name='Money_Spent'),
                 x='Money_Spent', y='Country', color='Variable', notched=True,
                 category_orders={"Variable": ["Total domestic trips", "Overnight visitors (tourists)"]},
                 title="Notched Horizontal Box Plot: Money Spent by Tourists in Each Country (Colored by Variable)")
    
    # Display the plot using st.plotly_chart
    st.plotly_chart(fig)
