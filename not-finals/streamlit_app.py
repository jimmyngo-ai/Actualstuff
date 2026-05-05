import streamlit as st
from openai import OpenAI

#this program takes something to input and two different languages(Choices being: Japanese, Korean, Spanish, English, Chinese, or Greek) and output the first input in the two chosen languages.

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.subheader("Translator")
#Japanese, Korean, Spanish, English, Chinese, or Greek
user_input = st.text_input("Required! Enter something to translate: ")
language = st.selectbox("Required! Pick one:", ["Japanese", "Korean", "Spanish", "English", "Chinese", "Greek"])
language2 = st.selectbox("Pick one:", ["Japanese", "Korean", "Spanish", "English", "Chinese", "Greek"])
#the expedcted input is most likely less than a paragraph, but could theoretically be longer. There is not specifically defined length.

system_prompt = (
    "You are an AI translator capable of understanding most modern languages\n\n"
    "Rules\n"
    "- The user wants to translate " + user_input + " into both " + language + " and " + language2 + "\n"
    "- Your response should only be the two translations ALONG WITH the language translated to in " + user_input + ", nothing more.\n"
    "- The output of two languages should be in two SEPERATE lines\n"
    "- Any untranslatable text or non-existant languages should be considered as null and ignored. In the case of untranslatable text, output NOTHING for that language."
)

ton = st.button("Generate")

if ton == True:
    if user_input != "" and language != "" and language2 != "":
        chat_history = [
            {"role": "system", "content": system_prompt},
            {
                "role": "user",
                "content": "I want to translate" + user_input + " into both " + language + " and " + language2 + "."
            }
        ]

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=chat_history
        )

        assistant_reply = response.choices[0].message.content
        st.write(assistant_reply)
        chat_history.append({"role": "assistant", "content": assistant_reply})
    elif user_input != "" and language != "":
        chat_history = [
            {"role": "system", "content": system_prompt},
            {
                "role": "user",
                "content": "I want to translate" + user_input + " into both " + language + " and " + language2 + "."
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
        st.error("Please input into all areas.")