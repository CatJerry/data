import streamlit as st

st.title("Hello, hi")
user_input = st.text_input("dddddd")
if st.button("submit"):
    st.write(f"{user_input}먹을게요")