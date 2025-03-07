import streamlit as st
"""
Hi there friend! You came to your perfect virtual chill zone spot. If you are 
"""

# inp = input("What would you like ")

with open('./styles/style.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

st.page_link("app.py", label="Home", icon="🏠")
st.page_link("pages/page_1.py", label="Page 1", icon="1️⃣")
st.page_link("pages/page_2.py", label="Page 2", icon="2️⃣", disabled=True)