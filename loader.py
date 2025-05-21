from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter

def load_and_split(file_path):
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return splitter.split_documents(documents)
