import snowflake.connector
import streamlit as st
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

q1 = st.text_input('Write your query','')
st.button('Run Query')
if not q1:
    st.error('Please write a query')
else:
    my_cur.execute(q1)
    my_catalog = my_cur.fetchall()
    st.dataframe(my_catalog)
