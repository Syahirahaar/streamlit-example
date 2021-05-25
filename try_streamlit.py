import streamlit as st
import pandas as pd

st.markdown('hoho')

df = pd.read_csv('C:/Users/Syahirahar/Documents/GitHub/MyDataEngineeringProject/Invistico_Airline.csv').head(5)
st.write(df)
