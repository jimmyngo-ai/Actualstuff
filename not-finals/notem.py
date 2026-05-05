import streamlit as st
from openai import OpenAI
import time

# ============================================================
# Define all variables here
# ============================================================
client = OpenAI(
    api_key = st.secrets["OPENAI_API_KEY"]
)

# This code creates a debate thingamajig that has two characters of your choosing debate over whatever you want!
# the only things required from the user are the customization inputs and the click of a button!

st.title("Debate stuff")
st.subheader("This makes your days a little better, I guess")

tab1, tab2 = st.tabs(["Customization", "Viewing Area"])
with tab1:
    with st.form("Hey!"):
        col1, col2 = st.columns(2)
        with col2:
            debater_A = st.text_input("First debater's name")
            debater_B = st.text_input("Opposing debater's name")
                    
        with col1:
            side_1 = st.text_input("What's the first side?")
            side_2 = st.text_input("What's the second side?")
            
        but = st.form_submit_button("Personalize")
    if but == True:
        with col1:
            st.write(f"{debater_A} is a agressive person")
        with col2:
            st.write(f"{debater_B} is a meticulous and introspective person")
topic = f"{side_1} vs {side_2}"


A_prompt = f'''
You are {debater_A}, an agressive debater.\n
You are arguing for the topic: {topic} on the side of {side_1}  .\n
Your debate style is agressive.\n
Follow these rules:\n
- Present logical arguments with supporting evidence\n
- Directly address points made by your opponent\n
- Stay on topic and maintain your position\n
- Use violent tone in your responses\n
- Keep responses between 3-5 sentences\n
- Do not concede your position, but VERY BRIEFLY acknowledge valid counterpoints\n

Each response should include:\n
- A main argument or counterargument\n
- Supporting reasoning or evidence\n
- A question or challenge to your opponent\n
'''
B_prompt = f'''
You are {debater_B}, a debater focused on small cracks in the opponent's argument, always pointing out fallacies.\n
You are arguing for the topic: {topic} on the side of {side_2}.\n
Your debate style is introspective and pressure-focused.\n
Follow these rules:\n
- Present unbreakable, perfectly logical arguments with supporting evidence\n
- DIRECTLY address points made by your opponent\n
- Stay on topic and maintain your position\n
- Use questioning tone in your responses\n
- Keep responses between 3-5 sentences\n
- Do not concede your position, but VERY BRIEFLY acknowledge valid counterpoints.\n

Each response should include:\n
- A main argument or counterargument\n
- Supporting reasoning or evidence\n
- A question or challenge to your opponent\n
'''
if "chat_history_A" not in st.session_state:
    st.session_state.chat_history_A = []

if "chat_history_B" not in st.session_state:
    st.session_state.chat_history_B = []



with tab2:
    if but == True:
        if not st.session_state.chat_history_A:
            st.session_state.chat_history_A = [
                {"role": "system", "content": A_prompt},
                {"role": "user", "content": f"Give your opening statement on: {topic}. Please keep the statement under 100 words"}
            ]
        response_A = client.chat.completions.create(
            model="gpt-4o",
            messages=st.session_state.chat_history_A
        )
        message_A = response_A.choices[0].message.content
        st.session_state.chat_history_A.append({"role": "assistant", "content": message_A})
        if not st.session_state.chat_history_B:
            st.session_state.chat_history_B = [
                {"role": "system", "content": B_prompt},
                {"role": "user", "content": f"The topic is: {topic}. Your opponent says: {message_A}. Respond with your opening statement. Please keep the statement under 100 words"}
            ]
        response_B = client.chat.completions.create(
            model="gpt-4o",
            messages=st.session_state.chat_history_B
        )
        message_B = response_B.choices[0].message.content
        st.session_state.chat_history_B.append({"role": "assistant", "content": message_B})   
        
        st.subheader("Opening statements")
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"{debater_A}'s opening statement\n\n{message_A}")
        with col2:
            st.write(f"{debater_B}'s opening statement\n\n{message_B}")  
        for round in range(3):
            roun = int(round) + 1
            st.session_state.chat_history_A.append({
                "role": "user",
                "content": f"Your opponent said: {message_B}. Respond. Please keep the statement under 100 words"
            })
            response_A = client.chat.completions.create(
                model="gpt-4o",
                messages=st.session_state.chat_history_A
            )
            message_A = response_A.choices[0].message.content
            st.session_state.chat_history_A.append({
                "role": "assistant",
                "content": message_A
            })
            st.session_state.chat_history_B.append({
                "role": "user",
                "content": f"Your opponent said: {message_A}. Respond. Please keep the statement under 100 words"
            })
            response_B = client.chat.completions.create(
                model="gpt-4o",
                messages=st.session_state.chat_history_B
            )
            message_B = response_B.choices[0].message.content
            st.session_state.chat_history_B.append({
                "role": "assistant",
                "content": message_B
            })
            st.subheader(f"Round {roun}")
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"{debater_A} Round {roun} statement\n\n{message_A}")
            with col2:
                st.write(f"{debater_B} Round {roun} statement\n\n{message_B}")            
        st.session_state.chat_history_A.append({
                "role": "user",
                "content": f"Your opponent has said: {st.session_state.chat_history_B}. Respond with your closing statement. Please keep the statement under 100 words"
            })
        response_A = client.chat.completions.create(
            model="gpt-4o",
            messages=st.session_state.chat_history_A
        )
        message_A = response_A.choices[0].message.content
        st.session_state.chat_history_A.append({
            "role": "assistant",
            "content": message_A
        })
        st.session_state.chat_history_B.append({
            "role": "user",
            "content": f"Your opponent has said: {st.session_state.chat_history_A}. Respond with your closing statement. Please keep the statement under 100 words"
        })
        response_B = client.chat.completions.create(
            model="gpt-4o",
            messages=st.session_state.chat_history_B
        )
        message_B = response_B.choices[0].message.content
        st.session_state.chat_history_B.append({
            "role": "assistant",
            "content": message_B
        })
        st.subheader("Closing statements")
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"{debater_A}'s final statement\n\n{message_A}")
        with col2:
            st.write(f"{debater_B}'s final statement\n\n{message_B}")  


