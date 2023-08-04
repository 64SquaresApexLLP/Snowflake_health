import streamlit as st
import pandas as pd
import snowflake.connector
st.header('Snowflake Healthcare App')
my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
# run a snowflake query and put it all in a var called my_catalog
my_cur.execute("select * from SWEATSUITS")
my_catalog = my_cur.fetchall()
st.dataframe(my_catalog)
q1 = st.text_input('Write your query','Write the query here')
my_cur.execute(q1)
my_catalog = my_cur.fetchall()
st.dataframe(my_catalog)
