# chatbot page
import streamlit as st
import re 
import random
from eliza_Dictionary import *
with open('./styles/chat.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

st.page_link("main.py", label="Information About The App", icon="🏠")
st.page_link("pages/chat.py", label="Chat with your favorite coffee expert!", icon="1️⃣")
st.page_link("pages/team.py", label="About The Team", icon="2️⃣")

dictionary = Dictionary()
##this will contain  our dictionray
regex_dic = dictionary.regex_dic()
regex_answr = dictionary.regex_answr()




regexDic = {
    "greetings": r"(hi|hello)"
}

answersDic = {
    "greetings": ['Hi, this is Elisa, your favorite coffee expert! What can I help you with?', 'yo whatsap bro']
}

occuranceDec =  {
    "greetings": 5,
    "yo": 5,
    "types": 3


}

def find_occurence_matching(regexDec: dict, userInput: str):
    """
        this function find takes a dictionary of regex and perform the regex on
        the input of the user and returns a dict for each key and occurance
    """
    occuranceDec = {}
    for key,value in regexDic.items():
        # a list of matching regex words
        regexResult = re.findall(value,userInput)
        # length of the list
        occurrance = len(regexResult)
        occuranceDec[key] = occurrance
    
    return occuranceDec

def best_category_matching(occuranceDec: dict):
    """
        this function take an occurance dictionary and return the max occurance key
    """

    keys = [key for key,value in occuranceDec.items() if value == max(occuranceDec.values())]

    # what if two categories are equal in the number of matching?
    # you need to check the length of the keys? if len(keys) == 1: else:
    return str(keys[0])

def random_answer(bestMatching: str, answersDic: dict):
    """
        this function takes the best matching category and return a random answer from an
        answer dictionary
    """
    return answersDic[bestMatching][random.randint(0,len(answersDic[bestMatching]))]

