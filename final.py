import streamlit as st
from openai import OpenAI
import st_yled
import json

st_yled.init()
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# I used AI to initialize context in session state to prevent a NameError if the script runs before tab 2 is clicked.
if "context" not in st.session_state:
    st.session_state.context = ""

st_yled.set("container", "background_color", "#0055FF")

with st_yled.container():
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
    # I used AI to change chat_history from a string to a list so it is compatible with the OpenAI API and .append method.
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [] 

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
            form = st.form_submit_button("GENERATE OFFER")
       
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
        8. For counteroffers, if the recipient refuses to lower their price, create a compromise. A numerical compromise, such as a skewed average between the two prices.
        9. If the offer is simply unreasonable, humor the user, but give many indications that the user was the writer.
        10. If more than 50% of the inputs are in a different language, respond in that language. Otherwise, use English.

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
        - Contain NO markdown formatting
        - Contain no surrounding text outside the JSON object
        """

        st.session_state.chat_historyA = [
            {"role": "system", "content": system_prompt},
            {
                "role": "user",
                "content": " I," + st.session_state.user + " want to create an counteroffer addressed to" + st.session_state.op + " on the topic of " + st.session_state.topic + "."
            },
        ]
        
        # I used AI to remove the definition of chat_historyB from here because it caused an error by referencing 'context' before the user input it in tab 2.

        with st.sidebar:
                with st.form("i hate this"):
                    # I used AI to add list() and .keys() so the selectbox shows the iteration titles instead of a dictionary error.
                    choice = st.selectbox("Choose an iteration", list(st.session_state.reiterations.keys()))
                    show = st.form_submit_button("Select")

        if form:    
            fields = [st.session_state.format, st.session_state.goal, st.session_state.op, st.session_state.topic, st.session_state.price, st.session_state.user]
            if all(field.strip() != "" for field in fields):
                if st.session_state.iterations < 1:    
                    # I used AI to clear chat_history and start fresh when generating a brand new initial offer.
                    st.session_state.chat_history = [
                        {"role": "system", "content": system_prompt},
                        {
                            "role": "user",
                            "content": f"I, {st.session_state.user}, want to create an initial offer addressed to {st.session_state.op} on the topic of {st.session_state.topic}."
                        }
                    ]
                    
                    response = client.chat.completions.create(
                        model="gpt-4o",
                        messages=st.session_state.chat_historyA
                    )
                    
                    response_content = response.choices[0].message.content
                    st.session_state.chat_history.append({"role": "assistant", "content": response_content})

                    dictionary = json.loads(response_content)
                    st.title(st.session_state.titles[st.session_state.iterations])        
                    st.write(dictionary["subject"])
                    st.write(dictionary["email"])
                    st.session_state.reiterations[st.session_state.titles[st.session_state.iterations]] = dictionary
                    st.session_state.iterations += 1
                else:
                    st.error("Please refer to the counteroffer page for further inputs")
            else:
                st.error("Please input into all of the fields.")

        with tab2:
            with st.form("ARghhhhhhhhhh"):
                # I used AI to assign context to a unique key to keep the input separate from the processing.
                context_input = st.text_input("Context for their counter offer")
                butt = st.form_submit_button("GENERATE REBUTTAL")
                
                if butt:
                    if st.session_state.iterations == 0:
                        st.error("Please generate the initial offer on the first tab before sending counteroffers.")
                    elif context_input.strip() == "":
                        st.error("Please provide context for their counteroffer.")
                    else:
                        st.session_state.context = context_input
                        
                        user_message = {
                            "role": "user",
                            "content": f"The opposing negotiator responded with feedback based on the context of: {st.session_state.context}. Generate a follow up to reach our goal: {st.session_state.goal}"
                        }
                        st.session_state.chat_history.append(user_message)

                        response = client.chat.completions.create(
                            model="gpt-4o",
                            messages=st.session_state.chat_history
                        )

                        response_content = response.choices[0].message.content
                        st.session_state.chat_history.append({"role": "assistant", "content": response_content})

                        dictionary = json.loads(response_content)
                        current_title = st.session_state.titles[st.session_state.iterations]
                        
                        st.title(current_title)        
                        st.write(dictionary["subject"])
                        st.write(dictionary["email"])
                        
                        st.session_state.reiterations[current_title] = dictionary
                        st.session_state.iterations += 1
        with tab3:
            if show:
                if choice in st.session_state.reiterations:
                    st.write(st.session_state.reiterations[choice]["subject"])
                    st.write(st.session_state.reiterations[choice]["email"])
