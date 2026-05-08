import streamlit as st
from openai import OpenAI
import st_yled
import json

st_yled.init()
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
st.title("N I C E R")
st.subheader("Negotiator, For The Commoner")
tab1, tab2, tab3 = st.tabs(["Settings input", "Counteroffer input", "History"])


if "titles" not in st.session_state:
    st.session_state.titles = ["Initial offer","First counter","Second counter","Third counter","Fourth counter","Fifth counter","Sixth counter","Seventh counter","Eighth counter","Nineth counter", "Tenth counter","Eleventh counter","Twelfth counter","Thirteenth counter","Fourteenth counter","Fifteenth counter","Sixteenth counter","Seventeenth counter","Eighteenth counter","Nineteenth counter","Twentieth counter","Twenty-first counter","Twenty-second counter"]
if "iterations" not in st.session_state:
    st.session_state.iterations = 0
if "reiterations" not in st.session_state:
    st.session_state.reiterations = {}
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
            st.session_state.op = st.text_input("Opposing negotiatior")
        with col2:
            st.session_state.topic = st.text_input("Topic of negotiation")
            st.session_state.price = st.text_input("Asking price")
        st.session_state.user = st.text_input("Name")
        form = st.form_submit_button("GENERATE")

    # Had ChatGPT refine the prompt commentted underneath into a more specific and clear system prompt.         
    system_prompt = f"""
    You are an elite negotiation and communications specialist trained through extensive reinforcement and evaluation.

    Your sole objective is to generate a highly effective, strategically tailored response that maximizes the user's desired outcome while maintaining professionalism, clarity, and persuasive strength.

    # Context
    - Sender Name: {st.session_state.user}
    - Recipient: {st.session_state.op}
    - Communication Topic: {st.session_state.topic}
    - Desired Outcome: {st.session_state.goal}

    # Core Instructions
    1. Generate a response that is specifically optimized to achieve the stated desired outcome.
    2. Tailor tone, wording, structure, and persuasive framing to the negotiation context.
    3. Maintain a professional, confident, and concise communication style.
    4. Do not use emojis, slang, filler language, or unnecessary formatting.
    5. Avoid generic phrasing whenever possible.
    6. The response must sound natural, human, and context-aware.
    7. Do not include explanations, commentary, analysis, labels, or metadata outside the requested output structure.

    # Output Requirements
    Return the response ONLY in valid JSON format.

    Use the following schema exactly:

    {{
        "subject": "Concise professional subject line",
        "email": "Full email body text",
    }}

    # Example Output
    {{
        "subject": "Request to Finalize Revised Agreement Terms",
        "email": "Dear {st.session_state.op},\nAfter reviewing the proposed terms, I would like to discuss a revised structure that better aligns with both parties' objectives...\nBest regards,\nJane"
    }}

    The output MUST ALWAYS:
    - Be only a valid JSON
    - Include only the both required fields
    - Escape line breaks properly
    - Contain no markdown formatting
    - Contain no surrounding text outside the JSON object
    """

    # system_prompt = f"""
    #     You are a professional negotiator, refined through extensive testing and reinforcement, who's only goal is to create a perfectly tailored response to adhere to the user's request.\n\n
    #     Rules\n
    #     - The user, {st.session_state.user} wants to create an {st.session_state.topic} addressed to {st.session_state.op} on the topic of {st.session_state.topic}\n
    #     - The user wishes this email to enforce the other party to reach the agreement {st.session_state.goal}. The generated email should be directly tailored to reach the goal.\n
    #     Your response should only be the email, nothing more. Also, NO EMOJIS AND ONLY PROFESSIONAL LANGUAGE. \n
    # """
    if form == True:    
        if st.session_state.iterations <= 1:    
            chat_history = [
                {"role": "system", "content": system_prompt},
                {
                    "role": "user",
                    "content": " I," + st.session_state.user + " want to create an email addressed to" + st.session_state.op + " on the topic of " + st.session_state.topic + "."
                },
            ]

            response = client.chat.completions.create(
                model="gpt-4o",
                messages=chat_history
            )

            dictionary = json.loads(response.choices[0].message.content)
            st.title(st.session_state.titles[st.session_state.iterations])        
            st.write(dictionary["subject"])
            st.write(dictionary["email"])
            st.write(st.session_state.titles[st.session_state.iterations])
            st.session_state.reiterations[st.session_state.titles[st.session_state.iterations]] = dictionary
            st.session_state.iterations += 1
            st.write(st.session_state.reiterations)
        else:   
            chat_history = [
                {"role": "system", "content": system_prompt},
                {
                    "role": "user",
                    "content": " I," + st.session_state.user + " want to create an counteroffer addressed to" + st.session_state.op + " on the topic of " + st.session_state.topic + ". They previously offered"
                },
            ]

            response = client.chat.completions.create(
                model="gpt-4o",
                messages=chat_history
            )

            dictionary = json.loads(response.choices[0].message.content)
            st.title(st.session_state.titles[st.session_state.iterations])        
            st.write(dictionary["subject"])
            st.write(dictionary["email"])
            st.write(st.session_state.titles[st.session_state.iterations])
            st.session_state.reiterations[st.session_state.titles[st.session_state.iterations]] = dictionary
            st.session_state.iterations += 1
            st.write(st.session_state.reiterations)
    with tab2:
        with st.sidebar:
            choice = st.selectbox("Choose an iteration", st.session_state.reiterations)
            show = st.button("Select")
        if show == True:
            st.write(st.session_state.reiterations)
            st.write(st.session_state.reiterations[choice])
