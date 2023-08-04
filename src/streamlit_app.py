import streamlit as st
import pandas
import snowflake.connector
streamlit.header('Snowflake Healthcare App')
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
# run a snowflake query and put it all in a var called my_catalog
my_cur.execute("select * from databases")
my_catalog = my_cur.fetchall()
streamlit.dataframe(my_catalog)
st.sidebar.button("workloads)
