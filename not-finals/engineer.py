import streamlit as st

st.title("Class Poll")

py = 0
js = 0
c = 0
j = 0



with st.form("n"):
    fav = st.radio("What's your favorite programming language?", ["Python", "JavaScript", "C++", "Java"])
    st.form_submit_button("Vote")


if fav == "Python":
    py += 1
if fav == "JavaScript":
    js += 1
if fav == "C++":
    c += 1
if fav == "Java":
    j += 1

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("Python")
    st.header(str(py))
with col2:
    st.subheader("JavaScript")
    st.header(str(js))
with col3:
    st.subheader("C++")
    st.write(str(c))
with col4:
    st.subheader("Java")
    st.write(str(j))