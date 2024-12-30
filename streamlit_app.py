import streamlit as st
import requests



st.write("Hello "+ st.experimental_user.email)

x = st.slider("Select a value")
st.write(x,"squared is<img src=x>", x * x)
