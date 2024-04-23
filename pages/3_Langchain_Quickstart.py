import streamlit as st
from langchain.llms import Ollama

st.title("🦜🔗 Langchain Quickstart App using Ollama")

def generate_response(input_text):
    llm = Ollama(model="llama2")
    st.info(llm(input_text))


with st.form("my_form"):
    text = st.text_area("Enter text:", "What are 3 key advice for learning how to code?")
    submitted = st.form_submit_button("Submit")
    if submitted:
        generate_response(text)
