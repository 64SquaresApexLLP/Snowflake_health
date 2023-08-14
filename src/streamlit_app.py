import streamlit as st
import pandas as pd
import snowflake.connector
import streamlit_option_menu
from streamlit_option_menu import option_menu

html_code = """
<div style="text-align: center;">
    <div style="width: 60px; height: 60px; background-color: #007BFF; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 24px;">
        DB
    </div>
    <div style="margin-top: 10px; font-weight: bold;">Database</div>
</div>
"""

st.markdown(html_code, unsafe_allow_html=True)

with st.sidebar:
    selected = option_menu(
    menu_title = "Main Menu",
    options = ["Home","Warehouse","Query Optimization and Processing","Storage","Contact Us"],
    icons = ["house","book","envelope","activity"],
    menu_icon = "cast",
    default_index = 0,
    #orientation = "horizontal",
)
if selected == "Home":
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
    st.subheader(f"**You Have selected {selected}**")
    
if selected == "Contact":
    st.subheader(f"**You Have selected {selected}**")

