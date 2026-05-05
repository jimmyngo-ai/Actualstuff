from openai import OpenAI
import json
import time
import streamlit as st

# wiki that creates artcles to inform the reader of japanese culture and history. Utilizes multi-page functions and the sidebar.

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
st.header("Wiki")
st.subheader("This wiki creates various pages for your education on Japanese culture")
system_prompt = """
        You are an AI system that creates a JSON object that contains 5 nested dictionaries that each contain a page of a Wikipedia article.
        Rules\n
        - Page with key "1" is about Japanese involvment on WW2, page with key "2" is about Japanese culture, page with key "3" is about Japanese food, page with key "4" is about Japanese great travel places in Japan, and page with key "5" is about Japanese economical stats.\n
        - Your response should only be the article IN JSON FORMAT, nothing more. Not even this "```json". \n"
        - This is an example(SPECIFICALLY AN EXAMPLE, DO NOT USE THIS AS AN ACTUAL RESPONSE) output of if the topic was on Japanese involvement on WW2 and major military actions:
        Topic = 
    {"1" :    {\n
    "Name": "",\n
    "History": "",\n
    "Characteristics": "",\n
    "Trivia": ""\n
    },
    "2" :    
        {\n
    "Name": "",\n
    "History": "",\n
    "Characteristics": "",\n
    "Trivia": ""\n
    },
    "3" :    
        {\n
    "Name": "",\n
    "History": "",\n
    "Characteristics": "",\n
    "Trivia": ""\n
    },
    "4" :    
        {\n
    "Name": "",\n
    "History": "",\n
    "Characteristics": "",\n
    "Trivia": ""\n
    },
    "5" :    
        {\n
    "Name": "",\n
    "History": "",\n
    "Characteristics": "",\n
    "Trivia": ""\n
    }
}
"""

chat_history = [
    {"role": "system", "content": system_prompt},
    {
        "role": "user",
        "content": ""
    }
]

#used chat to fix the error of dictionary not storing between reruns correctly

if "state" not in st.session_state:
    st.session_state.state = False

if "response" not in st.session_state:
    st.session_state.response = None

if st.session_state.state == False:
    st.session_state.response = client.chat.completions.create(
                model="gpt-4o",
                messages=chat_history
            )
    st.session_state.state = True

if "stat" not in st.session_state:
    st.session_state.stat = False

if "dictionary" not in st.session_state:
    st.session_state.dictionary = None

if st.session_state.stat == False:
    st.session_state.dictionary = json.loads(
        st.session_state.response.choices[0].message.content
    )
    st.session_state.stat = True


dictionary = st.session_state.dictionary

with st.sidebar:
        #simple input, choose one of the options in the selectbox
        page = st.selectbox("Hi! Thanks for opening this wiki on the coolest country in existance, Japan. With one of the strongest economies and ancient roots, Japan is widely known for tradition in modernity. For more info on WW2, select 1. For info on culture, select 2. For info about food, select 3. For info on great travel places, select 4. For info on economical stats, select 5.", ["Home", "1", "2", "3", "4", "5"])

col1, col2 = st.columns(2)
if dictionary != "":

    
    #st.write(dictionary[page])
    if page in ["1","2","3","4","5"]:
        article = dictionary[page]
        with col1:
            st.write("Article name:", article["Name"])
            st.write("History:", article["History"])
        with col2:
            st.write("Characteristics:", article["Characteristics"])
            st.write("Trivia:", article["Trivia"])
        #used the chat to remove the inefficent block of elif statements
    elif page == "Home":
        st.write("")

    else:
        st.error("INVALID INPUT")
        # redundant