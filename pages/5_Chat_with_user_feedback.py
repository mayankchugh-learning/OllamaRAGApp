import streamlit as st
from streamlit_feedback import streamlit_feedback
import trubrics
from langchain.llms import Ollama

llm = Ollama(model="llama2")

st.title("📝 Chat with feedback (Trubrics) using Ollama")

"""
In this example, we're using [streamlit-feedback](https://github.com/trubrics/streamlit-feedback) and Trubrics to collect and store feedback
from the user about the LLM responses.
"""

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "How can I help you? Leave feedback to help me improve!"}
    ]
if "response" not in st.session_state:
    st.session_state["response"] = None

messages = st.session_state.messages
for msg in messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input(placeholder="Tell me a joke about sharks"):
    messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    response = llm.predict(prompt)

    st.session_state["response"] = response
    with st.chat_message("assistant"):
        messages.append({"role": "assistant", "content": st.session_state["response"]})
        st.write(st.session_state["response"])

if st.session_state["response"]:
    feedback = streamlit_feedback(
        feedback_type="thumbs",
        optional_text_label="[Optional] Please provide an explanation",
        key=f"feedback_{len(messages)}",
    )

    st.toast("Feedback recorded!", icon="📝")
    # This app is logging feedback to Trubrics backend, but you can send it anywhere.
    # The return value of streamlit_feedback() is just a dict.
    # Configure your own account at https://trubrics.streamlit.app/
    # if feedback and "TRUBRICS_EMAIL" in st.secrets:
    #     config = trubrics.init(
    #         email=st.secrets.TRUBRICS_EMAIL,
    #         password=st.secrets.TRUBRICS_PASSWORD,
    #     )
    #     collection = trubrics.collect(
    #         component_name="default",
    #         model="llama2",
    #         response=feedback,
    #         metadata={"chat": messages},
    #     )
    #     trubrics.save(config, collection)
    #     st.toast("Feedback recorded!", icon="📝")'''
