import streamlit as st
import streamlit_option_menu
from streamlit_option_menu import option_menu

import requests
import streamlit as st

data = requests.get("'http://3.111.58.87:5000/test'").json()

st.write(data)
selected = option_menu(
    menu_title =None,
    options = ["Home","Projects","Contact"],
    icons = ["house","book","envelope"],
    default_index = 0,
    orientation = "horizontal",

)
  
