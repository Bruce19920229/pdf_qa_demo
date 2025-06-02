import streamlit as st
import os
from pdf_tool import extract_and_split_pdf
from qa_chain import load_qa_chain
import tempfile

st.set_page_config(page_title="📚 Chat with a Long PDF", layout="wide")
st.title("📘 Chat with your PDF (GPT-4-Turbo RAG)")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    with st.spinner("Reading and indexing your PDF..."):
        docs = extract_and_split_pdf(tmp_path)
        qa_chain = load_qa_chain(docs)

    question = st.text_input("Ask a question about the PDF:")
    if question:
        with st.spinner("Thinking..."):
            response = qa_chain.run(question)
            st.write("🤖", response)