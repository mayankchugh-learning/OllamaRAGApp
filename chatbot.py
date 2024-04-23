from langchain.llms import Ollama
import streamlit as st


with st.sidebar:
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"


llm = Ollama(model="llama2")


# Streamlit UI setup
st.title("💬 Chatbot")
st.caption("🚀 A streamlit chatbot powered by Ollama LLM")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])


if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = llm.predict(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)

# Input fields
question = st.text_input("What is your question?")

# Button to process input
if st.button('Query Documents'):
    with st.spinner('Processing...'):
        answer = llm.predict(question)
        st.text_area("Answer", value=answer, height=300, disabled=True)