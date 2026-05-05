import streamlit as st
import openai

st.title("Mythical Creature Profile Builder")
st.header("Design your own legendary being")
with st.form("Design your own legendary being"):
    st.session_state.submitted = False
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Creature name")
        origin = st.text_input("World of origin")
    with col2:
        thing_type = st.selectbox("Creature Type", ["Dragon", "Spirit", "Robot", "Alien", "Unknown"])
        personality = st.radio("Personality Type", ["Aggressive", "Calm", "Mysterious", "Chaotic"])
        lifespan = st.number_input("Lifespan",
        min_value=1,
        max_value=10000,
        value=500
        )
    abilities = st.multiselect("Select Special Abilities", ["Fire Control", "Mind Reading", "Teleportation", "Invisiblity", "Super Strength"])
    lore = st.text_area("Write a short backstory")
    weakness = st.checkbox("Include a weakness")
    if weakness == True:
        weaknes = st.text_input("Weakness")
    submit = st.form_submit_button("Generate Profile")
    # if name or origin or thing_type
if submit == True:
    if name != "":
        if origin != "":
            if thing_type != "":
                if personality != "":
                    if lifespan != "":
                        if abilities != []:
                            with st.form("Weakness"):
                                if weakness == True:
                                    weaknes = st.text_input("Input the weakness") 
                                    mit = st.form_submit_button("FINISH HIM/HER/THEM!!!")
                            st.write("Name: ", name)
                            st.write("Origin: ", origin)
                            st.write("Type: ", thing_type)
                            st.write("Personaility: ", personality)
                            st.write("Lifespan: ", lifespan)
                            for i in range(len(abilities)):
                                st.write("-", abilities[i])
                            st.write("Lore: ", lore)
                            st.warning("Weakness: ", weaknes)
                            reset = st.button("Reset builder?")
                            if reset == True:
                                st.rerun()
                            else:
                                st.warning("No weakness, No problem!")
                        else:
                            st.error("Please input into all areas")
                    else:
                        st.error("Please input into all areas")
                else:
                    st.error("Please input into all areas")
            else:
                st.error("Please input into all areas")
        else:
            st.error("Please input into all areas")
    else:
        st.error("Please input into all areas")
else:
    st.error("Please input into all areas")



