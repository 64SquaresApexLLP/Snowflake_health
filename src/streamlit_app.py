import streamlit as st
import streamlit_option_menu
from streamlit_option_menu import option_menu

import requests

def main():
    st.title("Streamlit API Example")
    
    # Make an API call
    response = requests.get("http://3.111.58.87:5000/test")
    
    if response.status_code == 200:
        data = response.json()
        st.write("API Response Data:")
        st.write(data)
    else:
        st.error("Failed to retrieve data from the API.")

if __name__ == "__main__":
    main()
  
