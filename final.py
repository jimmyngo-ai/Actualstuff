import streamlit as st
from openai import OpenAI
import st_yled

st_yled.init()

st.title("N I C E R")
st.subheader("Negotiator, For The Commoner")
tab1, tab2, tab3 = st.tabs(["Original settings", "Subsequent settings", "History"])

if "iterations" not in st.session_state:
    st.session_state.iterations = []
if "format" not in st.session_state:
    st.session_state.format = ""
if "goal" not in st.session_state:
    st.session_state.goal = ""
if "topic" not in st.session_state:
    st.session_state.topic = ""
if "price" not in st.session_state:
    st.session_state.price = ""
if "user" not in st.session_state:
    st.session_state.user = ""
if "op" not in st.session_state:
    st.session_state.op = ""

with tab1:
    with st.form("heyyy"):
        col1,col2 = st.columns(2)
        with col1:
            st.session_state.format = st.text_input("Communication format")
            st.session_state.goal = st.text_input("Goal input")
        with col2:
            st.session_state.topic = st.text_input("Topic of negotiation")
            st.session_state.price = st.text_input("Asking price")
        st.session_state.user = st.text_input("Name")
        form = st.form_submit_button("GENERATE")
system_prompt = (
    "You are a professional negotiator, refined through extensive testing and reinforcement, who's only goal is to create a perfectly tailored response to adhere to the user's request.\n\n"
    "Rules\n"
    "- The user," + st.session_state.user + " wants to create an " + st.session_state.topic + " to " + st.session_state.op + " on the topic of " + st.session_state.topic"
    "- The user wishes this email to enforce the "
    "Your response should only be the email, nothing more. Also, NO EMOJIS AND ONLY PROFESSIONAL LANGUAGE. \n"
)


chat_history = [
    {"role": "system", "content": system_prompt},
    {
        "role": "user",
        "content": " I," + user + " want to create an email to" + recip_name + " on the topic of " + topic + " in " + language + " that is " + str(length) +  " words. I want it in a " + style + " style.\n"
    }
]

response = client.chat.completions.create(
    model="gpt-4o",
    messages=chat_history
)

print(response)

with tab2:
    with st.form("heyy"):
        counter = st.text_input("Counter offer")
        form = st_yled.form_submit_button("GENERATE")
with tab3:
    with st.sidebar:
        st.selectbox("Choose an iteration", st.session_state.iterations)