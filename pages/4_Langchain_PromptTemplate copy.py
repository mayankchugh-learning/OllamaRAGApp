import streamlit as st
from langchain.llms import Ollama
from langchain.prompts import PromptTemplate

st.title("🦜🔗 Langchain - Blog Outline Generator App using Ollama")

def blog_outline(topic):
    # Instantiate LLM model
    llm = Ollama(model="llama2")
    # Prompt
    template = "As an experienced data scientist and technical writer, generate an outline for a blog about {topic}."
    prompt = PromptTemplate(input_variables=["topic"], template=template)
    prompt_query = prompt.format(topic=topic)
    # Run LLM model
    response = llm(prompt_query)
    # Print results
    return st.info(response)


with st.form("myform"):
    topic_text = st.text_input("Enter prompt:", "")
    submitted = st.form_submit_button("Submit")
    if submitted:
        blog_outline(topic_text)
