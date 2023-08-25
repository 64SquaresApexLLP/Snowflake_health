import streamlit as st
import streamlit_option_menu
from streamlit_option_menu import option_menu


    selected = option_menu(
    menu_title =None,
    options = ["Home","Projects","Contact"],
    icons = ["house","book","envelope"],
    default_index = 0,
    orientation = "horizontal",

    )
  
