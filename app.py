import os
import streamlit as st
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_pinecone import PineconeVectorStore

from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

from src.helper import download_hugging_face_embeddings
from src.prompt import system_prompt

# -----------------------------
# Load Environment Variables
# -----------------------------
load_dotenv()

# -----------------------------
# Load Embeddings & Vector Store
# -----------------------------
embeddings = download_hugging_face_embeddings()

index_name = "medical-chatbot"

docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

retriever = docsearch.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)

# -----------------------------
# Load LLM
# -----------------------------
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

# -----------------------------
# Prompt
# -----------------------------
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}")
    ]
)

question_answer_chain = create_stuff_documents_chain(
    llm,
    prompt
)

rag_chain = create_retrieval_chain(
    retriever,
    question_answer_chain
)

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(
    page_title="Medical Chatbot",
    page_icon="🩺",
    layout="centered"
)

st.title("🩺 Medical Chatbot")

# -----------------------------
# Chat History
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display old messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# Chat Input
# -----------------------------
user_question = st.chat_input(
    "Ask a medical question..."
)

if user_question:

    # Show user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_question
        }
    )

    with st.chat_message("user"):
        st.markdown(user_question)

    # Generate response
    with st.chat_message("assistant"):

        with st.spinner("Searching medical knowledge base..."):

            response = rag_chain.invoke(
                {"input": user_question}
            )

            answer = response["answer"]

            st.markdown(answer)

    # Save assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )