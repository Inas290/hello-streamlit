import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from a CSV file
df = pd.read_csv("https://raw.githubusercontent.com/Inas290/hello-streamlit/main/dataset-v2.csv")

# Create a Streamlit app
st.set_page_config(
    page_title="Tourism Dataset",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
)

st.sidebar.title("Navigation")
user_menu = st.sidebar.radio(
    'Select an Option',
    ('Home Page', 'Tourism per Country', 'Tourism per Stay Type')
)

if user_menu == 'Home Page':
    # Display title, description, and photo for the Home Page
    st.title("Tourism")
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
        # yearly_data = yearly_data.apply(lambda x: x.str.replace(',', '').astype(float))

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
        st.pyplot(plt.figure(figsize=(10, 6)))
        sns.boxplot(x='Category', y='Value', data=data_variable)
        plt.title(f'Box Plot of {variable} by Category')
        plt.xticks(rotation=45)
        plt.grid(True)

    # Create the notched horizontal box plot
    st.title('Retail Sales Analysis')
    st.subheader("Notched Horizontal Box Plot: Total Amount vs. Product Category (Colored by Gender)")
    fig = px.box(retail_data, x="Total Amount", y="Product Category", orientation="h", color="Gender", notched=True,
                 category_orders={"Product Category": ["Category1", "Category2", "Category3", "Category4"]},
                 title="Notched Horizontal Box Plot: Total Amount vs. Product Category (Colored by Gender)")

    st.plotly_chart(fig)

    # Add marginal plots (violin plot and box plot)
    st.subheader("Marginal Plots")
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))
    sns.violinplot(data=retail_data, x="Gender", y="Total Amount", ax=axs[0])
    axs[0].set_title("Violin Plot")
    sns.boxplot(data=retail_data, x="Gender", y="Age", ax=axs[1])
    axs[1].set_title("Box Plot")
    st.pyplot(fig)
