from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain.chains import RetrievalQA

import os

# Set up vector store
def store_documents(docs, persist_directory="db"):
    embedding = OllamaEmbeddings(model="nomic-embed-text")
    vectorstore = Chroma.from_documents(docs, embedding=embedding, persist_directory=persist_directory)
    return vectorstore  # .persist() is no longer needed

# Load stored vector DB
def load_vectorstore(persist_directory="db"):
    embedding = OllamaEmbeddings(model="nomic-embed-text")  # Ensure it matches what was used in store
    return Chroma(persist_directory=persist_directory, embedding_function=embedding)

# Create QA chain with a valid model
def get_qa_chain(vectorstore):
    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})
    llm = OllamaLLM(model="llama2:latest")  # Updated class name
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=True)

    def custom_run(query):
        result = qa_chain.invoke(query)  # ← use `invoke()` instead of calling the chain directly
        return result['result']

    return custom_run
