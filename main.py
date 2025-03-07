# Information page
import streamlit as st
import time
with open('./styles/main.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)


st.title("Welcome to our project ☕")



st.markdown(
    '''
    <div class="text-box">
        <p class="animated-text">Enjoy your coffee experience with our chatbot!</p>
    </div>
    ''',
    unsafe_allow_html=True
)