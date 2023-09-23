import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.title('Retail Sales Analysis')

# Load your retail sales dataset
RETAIL_DATA_PATH = 'https://github.com/Inas290/hello-streamlit/raw/main/data/retail_sales_dataset.csv'

@st.cache_data
def load_retail_data():
    data = pd.read_csv(RETAIL_DATA_PATH)
    return data

retail_data = load_retail_data()

# Create the notched horizontal box plot
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

# Load your fraud dataset
FRAUD_DATA_PATH = 'https://github.com/Inas290/hello-streamlit/raw/main/data/fraud1.csv'

@st.cache_resource
def load_fraud_data():
    data = pd.read_csv(FRAUD_DATA_PATH)
    data['trans_date_trans_time'] = pd.to_datetime(data['trans_date_trans_time'])  # Convert to datetime
    return data

fraud_data = load_fraud_data()

# Create the choropleth map
st.title('Fraud Transaction Choropleth Map')
st.subheader("Choropleth Map: Transaction Amount by State")

fig = px.choropleth(fraud_data,
                    locations="state",
                    color="amt",
                    hover_name="merchant",
                    animation_frame="trans_date_trans_time",
                    color_continuous_scale=px.colors.sequential.Plasma,
                    locationmode="USA-states",
                    title="Choropleth Map: Transaction Amount by State")

# Add background USA map
fig.update_geos(
    visible=False,
    scope="usa",
    showcoastlines=True,
)

# Modify the background map style
fig.update_geos(
    lataxis_range=[24, 50],  # Adjust latitude axis range for a better view
    lonaxis_range=[-125, -66],  # Adjust longitude axis range for a better view
    showland=True,
    landcolor="rgb(243, 243, 243)",  # Background color for land
    showlakes=True,
    lakecolor="rgb(255, 255, 255)",  # Background color for lakes
    showocean=True,
    oceancolor="rgb(230, 255, 255)",  # Background color for oceans
)

st.plotly_chart(fig)