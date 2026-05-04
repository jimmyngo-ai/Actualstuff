import streamlit as st
from openai import OpenAI
import st_yled

st_yled.init()

st.title("N I C E R")
st.subheader("Negotiator, For The Commoner")
tab1, tab2, tab3 = st.tabs(["Original settings", "Subsequent settings", "History"])

if "iterations" not in st.session_state:
    st.session_state.iterations = []

with tab1:
    with st.form("heyyy"):
        col1,col2 = st.columns(2)
        with col1:
            st.session_state.format = st.text_input("Communication format")
            goal = st.text_input("Goal input")
        with col2:
            topic = st.text_input("Topic")
            price = st.text_input("Asking price")
        form = st.form_submit_button("GENERATE")
with tab2:
    with st.form("heyy"):
        counter = st.text_input("Counter offer")
        form = st_yled.form_submit_button("GENERATE")
with tab3:
    with st.sidebar:
        st.selectbox("Choose an iteration", st.session_state.iterations)