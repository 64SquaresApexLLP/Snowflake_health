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
    c1, c2= st.columns(2)
    c3, c4= st.columns(2)
    
    with st.container():
        c1.write("c1")
        c2.write("c2")
    
    with st.container():
        c3.write("c3")
        c4.write("c4")
    
    with c1:
        df=pd.read_csv("world-data-2023.csv",columns=["Country","Density"])
        st.write(df)
        
       
    with c2:
        chart_data = pd.DataFrame(np.random.randn(20, 3),columns=["a", "b", "c"])
        st.bar_chart(chart_data)
    
    with c3:
        
        chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
        st.line_chart(chart_data)
    
    with c4:
        chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
        st.line_chart(chart_data)
if selected == "Contact":
    st.subheader(f"**You Have selected {selected}**")

