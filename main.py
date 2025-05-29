import streamlit as st

st.title("Autenticación")

if st.button("Autenticación"):
    st.login("google")

st.json(st.experimental_user)
st.write(f"Hello, {st.user.name}!")

