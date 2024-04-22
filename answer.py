from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OllamaEmbeddings
from langchain.vectorstores import Chroma

# Load the text file from your local path
loader = TextLoader("unique_data.txt")
raw_doc = loader.load()

# Split the text file content into chunks
text_splitter = CharacterTextSplitter(chunk_size=390, chunk_overlap=0)
splitted_docs = text_splitter.split_documents(raw_doc)

# Use embedding function to store them in vector db
ollamaEmbeddings = OllamaEmbeddings(model="llama2:7b-chat-q4_0")

# used chroma vector db to store the data
vectorstore = Chroma.from_documents(
    documents=splitted_docs,
    embedding=ollamaEmbeddings,
    persist_directory="./vector/my_data",
)

# This will write the data to local
vectorstore.persist()

# Verify
question = "What is KruKroKra?"
docs = vectorstore.similarity_search(question)

print(len(docs))
print(docs[0])