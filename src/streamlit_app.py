import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# import snowflake.connector
# import streamlit_option_menu
# from streamlit_option_menu import option_menu

price_df = pd.read_csv('src/wfp_food_prices_hti.csv', header=0,  skiprows=[1,])
current_data = price_df.sort_values(by=['date'])
all_departement = ['all'] + list(price_df['admin1'].unique())
all_market = ['all'] + list(price_df['market'].unique())
all_price = ['HTG', 'USD']
st.set_page_config(page_title='HAITI -  Cereal Price',
                   layout='wide', page_icon=':cereal:')
t1, t2 = st.columns((0.01, 1.08))

# t1.image('haiti-flag-square.jpg', width=120)
t2.title("Maize and Rice price evolution in Haiti")
t2.markdown(" **tel:** 509 36055983 **| email:** mailto:vitalralph@hotmail.com")
t2.markdown(" **data source:** WFP - World Food Programme")

disable = False
with st.sidebar:
    st.write('Parameters: ')
    d_option = st.selectbox(
        "Choose a department",
        tuple(all_departement),
    )
    if d_option == 'all':
        disable = True
    else:
        disable = False
        select_department = price_df[price_df['admin1'] == d_option]
        current_data = select_department.sort_values(by=['date'])
        select_market_df = select_department['market'].unique()
        all_market = select_market_df

    m_option = st.selectbox(
        "Choose a market",
        tuple(all_market),
        disabled=disable
    )

    p_option = st.selectbox(
        "Choose a currency",
        tuple(all_price),
    )


if d_option in all_departement:

    # Create a row layout
    c1, c2 = st.columns(2)
    c3, c4 = st.columns(2)

   # with st.container():
   #     c1.write("c1")
   #     c2.write("c2")

   # with st.container():
   #     c3.write("c3")
   #     c4.write("c4")
    if p_option == 'HTG':
        y = "price"
    else:
        y = "usdprice"
    with c1:
        mais_data = current_data[current_data['commodity']
                                 == 'Maize meal (local)']
        unit = mais_data['unit'].unique()[0] if len(
            mais_data['unit'].unique()) else None
        c_fig = px.line(mais_data, x='date', y=y,
                        title=f'Maize meal (local) in {p_option} ({unit})')
        st.plotly_chart(c_fig)

    with c4:
        rice_data = current_data[current_data['commodity']
                                 == 'Rice (imported)']
        unit = rice_data['unit'].unique()[0] if len(
            rice_data['unit'].unique()) else None
        r_fig = px.line(rice_data, x='date', y=y,
                        title=f'Rice (imported) in {p_option} ({unit})')
        st.plotly_chart(r_fig)

    with c3:
        wheat_data = current_data[current_data['commodity']
                                  == 'Rice (local)']
        unit = wheat_data['unit'].unique()[0] if len(
            wheat_data['unit'].unique()) else None
        w_fig = px.line(wheat_data, x='date', y=y,
                        title=f'Rice (local) in {p_option} ({unit})')
        st.plotly_chart(w_fig)

    with c2:
        m_i_data = current_data[current_data['commodity']
                                == 'Maize meal (imported)']
        unit = m_i_data['unit'].unique()[0] if len(
            m_i_data['unit'].unique()) else None
        mi_fig = px.line(m_i_data, x='date', y=y,
                         title=f'Maize meal (imported) in {p_option} ({unit})')
        st.plotly_chart(mi_fig)

st.write("1 marmite ~ 1.1lbs")
# fig_m = px.line(malaria_df, x='YEAR (DISPLAY)', y="Numeric", title=m_title)

# Contact Form

# with st.expander("Contact us", expanded=True):
#     with st.form(key='contact', clear_on_submit=True):

#         email = st.text_input('Contact Email')
#         text = st.text_area(
#             "Query", "Please fill in all the information or we may not be able to process your request")

#         submit_button = st.form_submit_button(label='Send Information')

# if submit_button:
#     st.write(f"{email}")
