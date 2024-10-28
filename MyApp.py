# Create an Interactive Data Analytics Portal with Streamlit in 7 Steps

import pandas as pd 
import plotly.express as px
import streamlit as st   

st.set_page_config(
    page_title='Consoleflare Analytics Portal',
    page_icon='📊'
)

st.title(':rainbow[Data Analytics Portal]')
st.subheader(':gray[Explore Data with ease.]',divider='rainbow')

file = st.file_uploader('Drop csv or excel file', type=['csv', 'xlsx'])
if file:
    if file.name.endswith('csv'):
        data = pd.read_csv(file)
    else:
        data = pd.read_excel(file)
    st.dataframe(data)
    st.info('File is successfully Uploaded', icon='🚨')