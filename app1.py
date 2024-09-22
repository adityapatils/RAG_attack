# Explanation of Each Step:
# Import Libraries: Essential libraries are imported for Streamlit and Langchain functionalities.
# Load Environment Variables: Load configuration from a .env file, if necessary.
# Set Title: Display a title for the Streamlit app.
# Load PDF: Load the IT resumes from a specified PDF file.
# Split Text: Split the PDF content into smaller chunks for easier processing.
# Create Vector Store: Store the document chunks in a vector format for efficient retrieval.
# Set Up Retriever: Configure a retriever to find relevant chunks based on similarity to user queries.
# Initialize Language Model: Set up the language model for generating responses to user questions.
# Get User Input: Use a chat input widget to capture user queries.
# Define System Prompt: Create a structured prompt that guides the model in answering questions.
# Process Query: If the user submits a query, generate a response using the RAG framework and display it.

import streamlit as st
import time
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate




from dotenv import load_dotenv
load_dotenv()


st.title("Explore IT Resumes Powered by Gemini RAG")

loader = PyPDFLoader("IT_resumes.pdf")
data = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000)
docs = text_splitter.split_documents(data)


vectorstore = Chroma.from_documents(documents=docs, embedding=GoogleGenerativeAIEmbeddings(model="models/embedding-001"))

retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 10})

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro",temperature=0,max_tokens=None,timeout=None)


query = st.chat_input("Say something: ") 
prompt = query

system_prompt = (
    "You are an assistant for question-answering tasks. "
    "Use the following pieces of retrieved context to answer "
    "the question. If you don't know the answer, say that you "
    "don't know. Use three sentences maximum and keep the "
    "answer concise."
    "\n\n"
    "{context}"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

if query:
    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)

    response = rag_chain.invoke({"input": query})
    #print(response["answer"])

    st.write(response["answer"])


