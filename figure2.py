import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from a CSV file
df = pd.read_csv("Name of file.csv")

# Create a Streamlit app
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

Original file is located at
    https://colab.research.google.com/drive/1L9dETODQRURUL3ArBk6aLQAYi32e9hT3
"""

