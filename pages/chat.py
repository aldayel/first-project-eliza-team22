import streamlit as st
import json
import backend.chat_utils as ct

# Load CSS
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