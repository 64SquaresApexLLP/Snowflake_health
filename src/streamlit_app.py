import streamlit as st
import pandas as pd

    # Title of the web app
st.title("Custom Layout Example")

    # Create a sidebar
st.sidebar.header("Sidebar")

    # Sidebar widgets
selected_option = st.sidebar.selectbox("Select an option", ["Option 1", "Option 2", "Option 3"])

    # Main content area
st.subheader("Main Content")

    # Conditional content based on the selected option
if selected_option == "Option 1":
    st.write("You selected Option 1.")
elif selected_option == "Option 2":
    st.write("You selected Option 2.")
else:
    st.write("You selected Option 3.")

    # Create a row layout
st.subheader("Row Layout")

col1, col2, col3 = st.columns(3)  # Divide the page into 3 columns

    # Widgets in the first column
with col1:
    st.write("Column 1")
    st.button("Button 1")

    # Widgets in the second column
with col2:
    st.write("Column 2")
    st.button("Button 2")

    # Widgets in the third column
with col3:
    st.write("Column 3")
    st.button("Button 3")



