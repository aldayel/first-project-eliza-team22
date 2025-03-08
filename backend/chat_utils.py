import re 
import random

def clear_chat_history():
    """Clears chat history when the app is first loaded by truncating the files."""
    try:
        open("./files/userPrompts.txt", "w").close()
        open("./files/chatAnswers.txt", "w").close()
    except Exception as e:
        print(f"Error clearing chat history: {e}")

def load_chat_history():
    try:
        with open("./files/userPrompts.txt", "r+") as f:
            user_prompts = f.readlines()
        with open("./files/chatAnswers.txt", "r+") as f:
            chat_answers = f.readlines()
        return user_prompts, chat_answers
    except FileNotFoundError:
        return [], []

# Save user input and bot response
def save_chat(prompt, answer):
    with open("./files/userPrompts.txt", "a") as f:
        f.write(f"{prompt}\n")
    with open("./files/chatAnswers.txt", "a")  as f:
        f.write(f"{answer}\n")

def find_occurence_matching(regexDec: dict, userInput: str):
    """
        this function find takes a dictionary of regex and perform the regex on
        the input of the user and returns a dict for each key and occurance
    """
    occuranceDec = {}
    for key,value in regexDec.items():
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

    # Check if all regex found no matching
    occuranceValues = [value for value in occuranceDec.values()]

    allZeros = True
    for value in occuranceValues:
        if value != 0:
            allZeros = False

    if allZeros:
        return "Unknown"
    else:
        # Find the best category that have matches
        keys = [key for key,value in occuranceDec.items() if value == max(occuranceDec.values())]
        return str(keys[0])


    # what if two categories are equal in the number of matching?
    # you need to check the length of the keys? if len(keys) == 1: else:
    

def random_answer(bestMatching: str, answersDic: dict):
    """
        this function takes the best matching category and return a random answer from an
        answer dictionary
    """
    return answersDic[bestMatching][random.randint(0,len(answersDic[bestMatching])-1)]
