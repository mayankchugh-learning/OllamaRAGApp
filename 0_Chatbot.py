from langchain.llms import Ollama
import streamlit as st



llm = Ollama(model="llama3")

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

