import streamlit as st
from streamlit_option_menu import option_menu

 

with st.sidebar:
  selected = option_menu(
    menu_title = "Main Menu",
    options = ["Home","Projects","Contact"],
    icons = ["house","book","envelope"],
    menu_icon = "cast",
    default_index = 0,

  )
  if selected == "Home":
    st.title(f"You Have selected {selected}")
  if selected == "Projects":
    st.title(f"You Have selected {selected}")
  if selected == "Contact":
    st.title(f"You Have selected {selected}")
