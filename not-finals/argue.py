import streamlit as st
from openai import OpenAI
import time

# ============================================================
# Define all variables here
# ============================================================
client = OpenAI(
    api_key = st.secrets["OPENAI_API_KEY"]
)
debater_A = "Leo"
debater_B = "Charlie"

print("Welcome to the Debate SIMULATOR!\n")

side_1 = st.text_input("What is the first side:")
side_2 = st.text_input("What is the second side:")
topic = side_1 + "or" + side_2


A_prompt = """
You are """ + debater_A + """, an agressive debater.\n
You are arguing for the topic: """ + topic + """ on the side of """ + side_1 + """.\n
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
"""
B_prompt = """
You are """ + debater_B + """, a debater focused on small cracks in the opponent's argument, always pointing out fallacies.\n
You are arguing for the topic: """ + topic + """ on the side of """ + side_2 + """.\n
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
"""

# Store debate rounds
debate_rounds = []

# ============================================================
# Create opening statements / start debate history / add to history
# ============================================================
# Create person A chat history
chat_history_A = [
    {"role": "system", "content": A_prompt},
    {"role": "user", "content": f"Give your opening statement on: {topic}"}
]
# Generate person A opening statements
response_A = client.chat.completions.create(
    model="gpt-4o",
    messages=chat_history_A
)
# Adding what person A said to their history
message_A = response_A.choices[0].message.content
chat_history_A.append({"role": "assistant", "content": message_A})

# Create person B chat history
chat_history_B = [
    {"role": "system", "content": B_prompt},
    {"role": "user", "content": f"The topic is: {topic}. Your opponent says: {message_A}. Respond with your opening statement."}
]
# Generate person B opening statements
response_B = client.chat.completions.create(
    model="gpt-4o",
    messages=chat_history_B
)
# Adding what person B said to their history
message_B = response_B.choices[0].message.content
chat_history_B.append({"role": "assistant", "content": message_B})

# Conduct 3 rounds of rebuttals hp
# NOTE - You need to add what the other character said within the user_prompt so the characters know what their opponent replied with

print(f"{'='*60}")
print("Opening statements!")
print(f"{'='*60}\n")

print(debater_A)
print(f"" + message_A)
print(f"\n\n\n{debater_B}")
print(message_B)

for round_num in range(1, 4):
    print(f"\n{'='*60}")
    print(f"ROUND {round_num}")
    print(f"{'='*60}\n")
    
    # YOUR CODE HERE: 
    # 1. Generate Debater A's rebuttal w/ Debater B's opening statement included in prompt
    # 2. Add to Debater A's history
    # 3. Generate Debater B's response w/ Debater A's rebuttal included in propmt
    # 4. Add to Debater B's history
    

    chat_history_A = [
    {"role": "system", "content": A_prompt},
    {"role": "user", "content": f"What is your response to {debater_B}'s statement(s), which was/were: {chat_history_B}"}
    ]
    # Generate person A opening statements
    response_A = client.chat.completions.create(
        model="gpt-4o",
        messages=chat_history_A
    )
    # Adding what person A said to their history
    message_A = response_A.choices[0].message.content
    chat_history_A.append({"role": "assistant", "content": message_A})
 
    chat_history_B = [
    {"role": "system", "content": B_prompt},
    {"role": "user", "content": f"What is your response to {debater_A}'s statement(s), which was/were: {chat_history_A}"}
    ]
    # Generate person A opening statements
    response_B = client.chat.completions.create(
        model="gpt-4o",
        messages=chat_history_B
    )
    # Adding what person A said to their history
    message_B = response_B.choices[0].message.content
    chat_history_B.append({"role": "assistant", "content": message_B})

    print(debater_A)
    print(message_A)
    print("\n\n" + debater_B)
    print(message_B)

    time.sleep(1)
    
# YOUR CODE HERE: Generate closing statements for both debaters
print(f"{'='*60}")
print("Closing statements")
print(f"{'='*60}\n")
chat_history_A = [
{"role": "system", "content": A_prompt},
{"role": "user", "content": f"What is your final statement to {debater_B}'s statements, which were: {chat_history_B}? Make it one sentence."}
]
# Generate person A opening statements
response_A = client.chat.completions.create(
    model="gpt-4o",
    messages=chat_history_A
)
# Adding what person A said to their history
message_A = response_A.choices[0].message.content
chat_history_A.append({"role": "assistant", "content": message_A})

chat_history_B = [
{"role": "system", "content": B_prompt},
{"role": "user", "content": f"What is your final statement to {debater_A}'s statements, which were: {chat_history_A}? Make it one sentence."}
]
# Generate person A opening statements
response_B = client.chat.completions.create(
    model="gpt-4o",
    messages=chat_history_B
)
# Adding what person A said to their history
message_B = response_B.choices[0].message.content
chat_history_B.append({"role": "assistant", "content": message_B})


print(debater_A)
print(message_A)
print("\n\n" + debater_B)
print(message_B)


# The topic is fluid to the user input, the debaters are Leo and Charlie, being agressive and meticulous about small cracks in the opponent's argument respectively 