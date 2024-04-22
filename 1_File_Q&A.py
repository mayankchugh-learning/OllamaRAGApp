import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_community import embeddings
from langchain_community.llms import Ollama
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
import re
import os

# URL processing
def process_input(uploaded_file, question):
    model_local = Ollama(model="mistral")

    sentences = ""

    with open(uploaded_file, 'r', encoding="utf-8") as txt_file:
        text = txt_file.read()

        # Normalize whitespace and clean up text
        text = re.sub(r'\s+', ' ', text).strip()

        # Split text into chunks by sentences, respecting a maximum chunk size
        sentences = re.split(r'(?<=[.!?]) +', text)  # split on spaces following sentence-ending punctuation



    text_splitter=RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
    all_splits = text_splitter.split_documents(sentences)

    vectorstore = Chroma.from_documents(
        documents=sentences,
        collection_name="rag-chroma",
        embedding=embeddings.OllamaEmbeddings(model='nomic-embed-text')
    )
    retriever = vectorstore.as_retriever()
    
    #perform the RAG 
    
    after_rag_template = """Answer the question based only on the following context:
    {context}
    Question: {question}
    """
    after_rag_prompt = ChatPromptTemplate.from_template(after_rag_template)
    after_rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | after_rag_prompt
        | model_local
        | StrOutputParser()
    )


    return after_rag_chain.invoke(question)

# Streamlit UI setup

st.title("📝 File Q&A with Ollama")
st.write("Enter URLs (one per line) and a question to query the documents.")

# Input fields
uploaded_file = st.file_uploader("Upload an article", type=("txt", "md"))
question = st.text_input(
    "Ask something about the article",
    placeholder="Can you give me a short summary?",
    disabled=not uploaded_file,
)

# Button to process input
if st.button('Query Documents'):
    with st.spinner('Processing...'):
        answer = process_input(uploaded_file, question)
        st.text_area("Answer", value=answer, height=300, disabled=True)
        st.write("### Answer")
        st.write(answer)        