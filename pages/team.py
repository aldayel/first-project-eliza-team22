import streamlit as st
with open('./styles/team.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

st.page_link("main.py", label="Information About The App", icon="🏠")
st.page_link("pages/chat.py", label="Chat with your favorite coffee expert!", icon="1️⃣")
st.page_link("pages/team.py", label="About The Team", icon="2️⃣")

