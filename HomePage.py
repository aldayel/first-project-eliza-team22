import streamlit as st


page_bg_gradient = """
<style>
[data-testid="stAppViewContainer"] {
    background: #1e130c; 
    background: -webkit-linear-gradient(to left, #1e130c, #9a8478);
    background: linear-gradient(to left, #1e130c, #9a8478); 
}
</style>
"""


st.markdown(page_bg_gradient, unsafe_allow_html=True)


st.title("Welcome to my Coffee app")