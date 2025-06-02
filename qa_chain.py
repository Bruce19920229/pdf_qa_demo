from dotenv import load_dotenv
load_dotenv()
import os
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma
from langchain.prompts import PromptTemplate

def load_qa_chain(docs):
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma.from_documents(docs, embeddings)
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 3})

    prompt_template = """You are a helpful assistant answering questions based only on the context below.
If you don’t know the answer, just say you don’t know.

Context:
{context}

Question:
{question}

Answer:"""

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=prompt_template,
    )

    llm = ChatOpenAI(model="gpt-4-turbo", temperature=0)
    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=False,
        chain_type_kwargs={"prompt": prompt}
    )
    return chain