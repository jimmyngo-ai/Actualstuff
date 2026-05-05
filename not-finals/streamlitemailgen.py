import streamlit as st
from openai import OpenAI
import st_yled

# This program creates an email in the user's desired language and style, including the recipient and user's name for a well structured writing style
# Expected user input = Name, Recipient Name, Topic, Language of Email, Length of Email, Writing Style

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
st.header("Email Generator")
st.write("For the lazy")
with st.form("thing"):
    user = st.text_input("Input your name:")
    recip_name = st.text_input("Input the name of the recipient:")
    topic = st.text_area("Input the topic of the email:")
    language = st.selectbox("Choose a language", ["Japanese", "English", "Chinese", "Greek", "Arabic", "Vietnamese"])
    length = st.slider("Input the rough length of the email, in words:",
                       min_value=1,
                       max_value=300)
    style = st.selectbox("Choose a writing style", ["Formal", "Casual", "Business", "Insane", "Deadly", "Threateaning"])
    submit = st.form_submit_button("When done, press me!")

if submit == True:
    if user and recip_name and topic and language and length != "":
        system_prompt = (
            "You are an AI Email Generator\n\n"
            "Rules\n"
            "- The user," + user + " wants to create an email to" + recip_name + " on the topic of " + topic + ", with the email written in the language " + language + ".\n"
            "Your response should only be the email, nothing more. Also, NO EMOJIS\n"
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

        assistant_reply = response.choices[0].message.content
        st.write(assistant_reply)
        chat_history.append({"role": "assistant", "content": assistant_reply})
    else:
        st.error("Please fill out all areas!")
