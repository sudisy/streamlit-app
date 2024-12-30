import streamlit as st
import requests


email = st.experimental_user.email
st.write("Hello "+ str(email))

x = st.slider("Select a value")
st.write(x,"squared is<img src=x>", x * x)
