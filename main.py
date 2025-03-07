# Information page
import streamlit as st
"""
Hi there friend! You came to your perfect virtual chill zone spot. If you are 
"""

# inp = input("What would you like ")

with open('./styles/main.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

st.page_link("main.py", label="Information About The App", icon="🏠")
st.page_link("pages/chat.py", label="Chat with your favorite coffee expert!", icon="1️⃣")
st.page_link("pages/team.py", label="About The Team", icon="2️⃣")