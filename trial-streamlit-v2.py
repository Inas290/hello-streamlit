import streamlit as st
import pandas as pd

from Tabs.Name1 import Name1
from Tabs.Name2 import Name2

# Load the data from a CSV file
data = pd.read_csv("Name of file.csv")

# CREATE STREAMLIT APP
def main():
    st.set_page_config(
        page_title="Your App Title",
        page_icon=":chart_with_upwards_trend:",
        layout="wide",
    )

    st.sidebar.title("Navigation")
    user_menu = st.sidebar.radio(
        'Select an Option',
        ('Home Page', 'Title 1', 'Title 2')
    )

    if user_menu == 'Home Page':
        # Display title, description, and photo for the Home Page
        st.title("Title")
        st.write("Write description\nOther description")
        st.image("Media/Name.gif", use_column_width=True)

    elif user_menu == "Title 1":
        # Title for the "Title 1" tab
        st.title("Title of tab1")

        # Calling the function of the Name1 tab
        Name1(data)

    elif user_menu == "Title 2":
        # Title for the "Title 2" tab
        st.title("Title of tab2")

        # Calling the function of the Name2 tab
        Name2(data)

if __name__ == '__main__':
    main()