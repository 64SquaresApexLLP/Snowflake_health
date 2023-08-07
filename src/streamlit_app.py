import streamlit as st
import pandas as pd
import numpy as np

st.sidebar.header("Sidebar")

# Create a row layout
c1, c2= st.columns(2)
c3, c4= st.columns(2)

with st.container():
    c1.write("c1")
    c2.write("c2")

with st.container():
    c3.write("c3")
    c4.write("c4")

with c1:
    df=pd.read_csv("world-data-2023.csv")
    st.write(df['Country','Density'])
    
    
   
with c2:
    chart_data = pd.DataFrame(np.random.randn(20, 3),columns=["a", "b", "c"])
    st.bar_chart(chart_data)

with c3:
    
    chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
    st.line_chart(chart_data)

with c4:
    chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
    st.line_chart(chart_data)
    



