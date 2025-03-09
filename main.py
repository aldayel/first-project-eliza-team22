# Information page
import streamlit as st


with open('./styles/main.css') as f:
    css = f.read()


st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)


st.title("Welcome to Boneza ☕")



st.markdown(
    '''
    <div class="text-box">
        <p class="animated-text">Boneza is your guide to the world of coffee! Whether you want to explore new recipes, master the art of brewing, or learn about coffee’s benefits, Boneza has you covered. Enjoy a rich experience and discover the best ways to craft your perfect cup!
</p>
    </div>
    ''',
    unsafe_allow_html=True
)


