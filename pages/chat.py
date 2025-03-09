import streamlit as st
import json
import backend.chat_utils as ct

# Load CSS
import re 
import random
from backend.eliza_Dictionary import *

with open('./styles/chat.css') as f:
    css = f.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# Clear chat history: only on first page load
if "chat_initialized" not in st.session_state:
    # ct.clear_chat_history()  
    st.session_state.chat_initialized = True

# Load JSON files
with open("./files/regexDic.json", "r") as file:
    regexDic = json.load(file)

with open("./files/answersDic.json", "r") as file:
    answersDic = json.load(file)

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display previous chat messages from session state
for chat in st.session_state.chat_history:
    st.chat_message(chat["role"]).write(chat["message"])

# Handle new user input
prompt = st.chat_input("Ask me anything about coffee!")
if prompt:
    # Find answer
    occurance_dict = ct.find_occurence_matching(regexDic, prompt)
    key = ct.best_category_matching(occurance_dict)
    answer = ct.random_answer(key, answersDic)

    # Append messages to session state for persistence
    st.session_state.chat_history.append({"role": "user", "message": prompt})
    st.session_state.chat_history.append({"role": "assistant", "message": answer})

    # # Save new chat messages to file (optional for logging)
    # ct.save_chat(prompt, answer)

    # Display new messages
    st.chat_message("user").write(prompt)
    st.chat_message("assistant").write(answer)


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

