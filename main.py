import streamlit as st

st.title("Autenticación")

if st.button("Autenticación"):
    st.login("google")

st.json(st.experimental_user)
st.header(f"Hola{st.experimental_user.name}")

