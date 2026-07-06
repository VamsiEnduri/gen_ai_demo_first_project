import streamlit as st 
from groq import Groq

st.title("Gen-AI chatbot application")

question___=st.text_input("enter yr question",placeholder="enter yr question here to get the naswer")
pdf=st.file_uploader("upload pdf file ",type=["pdf"])

g_client=Groq(api_key="") # groq client

if st.button("Generate"):
    st.write(question___)
    res=g_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role":"user","content":question___}]
    ) # give you answer for yr question
    st.write(res.choices[0].message.content)

