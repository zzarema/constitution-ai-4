import os
import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader
from dotenv import load_dotenv

# Set API key
load_dotenv()
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Load Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

st.title("🇰🇿 Kazakhstan Constitution AI Assistant (Gemini)")
st.write("Ask questions about the Constitution or upload documents.")

# Load base constitution
def load_constitution():
    with open("constitution.txt", "r", encoding="utf-8") as f:
        return f.read()

constitution_text = load_constitution()
full_text = constitution_text

# File uploader
uploaded_files = st.file_uploader("Upload .pdf or .txt files", type=["pdf", "txt"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        if file.type == "application/pdf":
            reader = PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            full_text += "\n" + text
        elif file.type == "text/plain":
            full_text += "\n" + file.read().decode("utf-8")
    st.success("Uploaded documents added to context.")

# Chat
query = st.text_input("Ask a question:")

if query:
    with st.spinner("Thinking..."):
        response = model.generate_content(f"{query}\n\nContext:\n{full_text}")
        st.write("### Answer:")
        st.write(response.text)
