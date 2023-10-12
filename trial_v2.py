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
    st.write("Tourism rates have exhibited fluctuating trends over the years, prompting the need for more comprehensive data analysis and an in-depth understanding of the contributing factors. These changes can be attributed to a multitude of variables, including economic conditions, geopolitical stability, environmental factors, and shifting travel preferences. Economic factors, such as changes in exchange rates and income levels, significantly influence people's travel decisions. Additionally, geopolitical events, like conflicts or changes in visa policies, can deter or attract tourists. Environmental concerns, such as natural disasters or climate change impacts, can affect the desirability of certain destinations. Furthermore, evolving consumer preferences, driven by trends like sustainable and experiential travel, add complexity to the equation. To truly comprehend these shifts in tourism rates, it is imperative to delve into extensive data analysis and consider the intricate interplay of these multifaceted variables.")
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

#elif user_menu == "Tourism per Stay Mode":
#    df = pd.DataFrame(df)

    # Streamlit app
#    st.title("Grouped Bar Plot")
#    st.write("Overnight tourism, historically a cornerstone of the tourism industry, is showing signs of diminishing significance in the broader landscape of travel. Increasingly, tourists are gravitating towards day trips and experiences that don't require an overnight stay. This shift can be attributed to a variety of factors, including the rise of spontaneous or short-term travel, the popularity of urban day trips, and the desire for more flexible and budget-conscious options. With the advent of advanced transportation systems and the ubiquity of online information, travelers can easily explore attractions and activities within easy reach of their home base. The modern tourist often prioritizes efficient use of time and resources, opting for day tours and excursions that allow them to explore multiple destinations in a shorter timeframe. Consequently, the tourism industry must adapt to this evolving trend and consider alternative approaches to engage and cater to this new breed of travelers who seek memorable experiences without the need for an overnight stay.")
#    st.subheader("Money Spent by Country and Variable")

    # Create a grouped bar plot
#    fig = px.bar(
#        df.melt(id_vars=["Country", "Variable"], var_name="Year", value_name="Money_Spent"),
#        x="Country",
#        y="Money_Spent",
#        color="Variable",
#        barmode="group",
#        title="Money Spent by Country and Variable"
#    )

    # Display the plot
#    st.plotly_chart(fig)

elif user_menu == "Tourism per Stay Mode":
    df = pd.DataFrame(df)

    # Streamlit app
    st.title("Grouped Bar Plot")
    st.subheader("Money Spent by Country and Variable")

    # Create a grouped bar plot with custom colors
    fig = px.bar(
        df.melt(id_vars=["Country", "Variable"], var_name="Year", value_name="Money_Spent"),
        x="Country",
        y="Money_Spent",
        color="Variable",
        barmode="group",
        title="Money Spent by Country and Variable"
    )

    # Customize the colors of the bars
    fig.update_traces(marker_color=["purple", "navy"])

    # Display the plot
    st.plotly_chart(fig)

