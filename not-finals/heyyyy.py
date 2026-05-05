import streamlit as st
from openai import OpenAI
import json
import time

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# this streamlit program allows for creation and storage of fictional pokemon. It can also sort them into alphabetical order(not saved but applicable when selected)! Very cool.
# we expect clicking buttons for alphabetizing and inputting of feasible names for the Chat to utilize and create pokemon based off of. Also, please dont hakk meh code.

system_prompt = """
You are a data-generation system.

Your task is to generate VALID JSON describing a fictional Pokémon based on a provided name.

STRICT OUTPUT RULES:
- Output ONLY valid JSON.
- Do NOT include explanations, markdown, backticks, or extra text.
- The JSON MUST be parseable by Python's json.loads().
- The top-level structure MUST be a JSON array.
- The array MUST contain EXACTLY 5 objects in the order shown below.
- Do NOT add or remove keys.
- Do NOT rename keys.
- Fill in all empty string values with appropriate content.

DATA RULES:
- Poke_ID must be EXACTLY 4 random digits (0–9).
- HP, Attack, Defense, and Speed must be integers between 0 and 15.
- Pokemon_type must contain 1 or 2 types only.
- All content must be fictional.

REQUIRED JSON STRUCTURE (FOLLOW EXACTLY):

[
  {
    "stats": {
      "HP": "",
      "Attack": "",
      "Defense": "",
      "Speed": ""
    },
    "Description": "",
    "Details": {
      "Gender": "",
      "Category": "",
      "Ability": {
        "Ability_1": "",
        "Ability_2": "",
        "Ability_3": ""
      }
    },
    "Pokemon_type": ""
  },
  {
    "Pokemon_weaknesses": ""
  },
  {
    "Evolution": ""
  },
  {
    "Poke_ID": ""
  },
  {
    "Name": ""
  }
]

REMEMBER:
- Return ONLY the JSON array.
- No surrounding text.
"""
# used ChatGPT to rewrite the prompt cleanly

def display(pokemon):
  
  st.write("Name: " + pokemon[4]["Name"])
  st.write("Poke ID: " + pokemon[3]["Poke_ID"])
  col1, col2, col3, col4, col5 = st.columns(5)
  with col1:
    st.write("HP: " + str(pokemon[0]["stats"]["HP"]))
    st.write("Attack: " + str(pokemon[0]["stats"]["Attack"]))
    st.write("Defense: " + str(pokemon[0]["stats"]["Defense"]))
    st.write("Speed: " + str(pokemon[0]["stats"]["Speed"]))
  with col2:
    st.write(pokemon[0]["Description"])
  with col3:
    st.write("Gender: " + pokemon[0]["Details"]["Gender"])
    st.write("Category: " + pokemon[0]["Details"]["Category"])
  with col4:
    st.write("Ability 1: " + pokemon[0]["Details"]["Ability"]["Ability_1"])
    st.write("Ability 2: " + pokemon[0]["Details"]["Ability"]["Ability_2"])
    st.write("Ability 3: " + pokemon[0]["Details"]["Ability"]["Ability_3"])
  with col5:
    st.write("PokeType: " + pokemon[0]["Pokemon_type"])
    st.write("Weaknesses: " + pokemon[1]["Pokemon_weaknesses"])
    st.write("Evolution: " + pokemon[2]["Evolution"])
  st.write("--------------------------------------------------")

if "p_al" not in st.session_state:
  st.session_state.p_al = []

tab1, tab2 = st.tabs(["View", "Create"])


with tab2:
  name = st.text_input("What would you like your pokemon's name to be:")
  submit = st.button("Submit")

  if submit:
    if name != "":  
      chat_history = [
          {"role": "system", "content": system_prompt},
          {"role": "user", "content": "Make the pokemon based on the name " + name + "."}
      ]

      response = client.chat.completions.create(
          model="gpt-4o",
          messages=chat_history
      )


      print(response.choices[0].message.content)

      # parse JSON
      dictionary = json.loads(response.choices[0].message.content)

      # append parsed data, not raw response
      st.session_state.p_al.append(dictionary)

      #used the chat to fix the problem of the dictionary not reading correctly.

      st.success(f"{name} added to your Pokédex!")
    else:
      st.error("Please input a thingymajig")
with tab1:
  if len(st.session_state.p_al) == 0:
      st.info("No Pokemon entries yet!")
  else:
      sort = st.radio("Do you want to sort by alphabetical order:", ["Yes", "No"])
      show = st.button("Show Pokemon")

      if show == True:
          if sort == "Yes":
              p_all = sorted(st.session_state.p_al, key=lambda p: p[4]["Name"].lower())
              # used the legnedary chat to fix the stupid sorting in the previous project
          else:
            p_all = st.session_state.p_al

          for i in range(len(p_all)):
            pokemon = p_all[i]
            display(pokemon)




#st.write(dictionary[page])