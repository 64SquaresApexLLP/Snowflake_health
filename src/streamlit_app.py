import snowflake.connector
import streamlit as st
my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT TABLE_SCHEMA,RETENTION_TIME FROM db_jay.information_schema.tables;")
my_data_row = my_cur.fetchone()
st.text("Hello from Snowflake:")
st.text(my_data_row)

