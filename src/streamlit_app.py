'''
import streamlit
import pandas
import snowflake.connector
streamlit.header('Snowflake Healthcare App')
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
# run a snowflake query and put it all in a var called my_catalog
my_cur.execute("select * from databases")
my_catalog = my_cur.fetchall()
streamlit.dataframe(my_catalog)
'''

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load the DataFrame
df = pd.read_csv('https://raw.githubusercontent.com/Kavy-gupta/first_streamlit_app/main/veg_plant_height.csv')

# Page title
st.title('Plant Data Visualization')

c1, c2= st.columns(2)

with st.container():
    c1.write("c1")
    c2.write("c2")
 
# 1. Bar Chart comparing 'plant_name' with 'Low_End_of_Range'
with c1:
  st.header('Bar Chart: Low End of Range')
  plt.figure(figsize=(10, 6))
  plt.barh( df['Low_End_of_Range'],df['plant_name'],)
  plt.ylabel('Plant Name') 
  plt.xlabel('Low End of Range')
  plt.xticks(rotation=90)
  st.pyplot(plt)


# 2. Bar Chart comparing 'plant_name' with 'High_End_of_Range'
with c2:
  st.header('Bar Chart: High End of Range')
  plt.figure(figsize=(10, 6))
  plt.barh( df['High_End_of_Range'],df['plant_name'],)
  plt.ylabel('Plant Name')
  plt.xlabel('High End of Range')
  plt.xticks(rotation=90)
  st.pyplot(plt)


