import streamlit as st
import pandas as pd
import snowflake.connector
import streamlit_option_menu
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
    st.header('Snowflake Healthcare App')
    my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
    my_cur = my_cnx.cursor()
    # run a snowflake query and put it all in a var called my_catalog
    my_cur.execute("select * from SWEATSUITS")
    my_catalog = my_cur.fetchall()
    st.dataframe(my_catalog)
    q1 = st.text_input('Write your query','')
    st.button('Run Query')
    if not q1:
      st.error('Please write a query')
    else:
      my_cur.execute(q1)
      my_catalog = my_cur.fetchall()
      st.dataframe(my_catalog)
  if selected == "Projects":
    st.title(f"You Have selected {selected}")
  if selected == "Contact":
    st.title(f"You Have selected {selected}")
