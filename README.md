# 🩺 Medical RAG Chatbot

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10-blue)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green)
![Groq](https://img.shields.io/badge/Groq-Llama--3.3--70B-orange)
![Pinecone](https://img.shields.io/badge/Pinecone-VectorDB-purple)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)

</p>

<p align="center">
An end-to-end Retrieval-Augmented Generation (RAG) system for medical question answering using LangChain, Pinecone, HuggingFace Embeddings, Groq Llama-3.3-70B, and Streamlit.
</p>

---

## 🚀 Overview

Medical RAG Chatbot is a domain-specific Generative AI application that retrieves relevant medical knowledge from a medical textbook and generates context-aware responses using Retrieval-Augmented Generation (RAG).

Unlike traditional chatbots that rely solely on LLM knowledge, this system performs semantic search over indexed medical documents and grounds responses using retrieved context from a vector database.

---

## ✨ Features

- 📄 Medical PDF ingestion and processing
- ✂️ Intelligent document chunking
- 🧠 Semantic embeddings using Sentence Transformers
- 🗄️ Pinecone Vector Database integration
- 🔍 Top-K similarity search
- 🤖 Groq-powered Llama-3.3-70B inference
- 🔗 LangChain Retrieval Chains
- 💬 Interactive Streamlit chat interface
- 📦 Modular project architecture

---

## 🏗️ System Architecture

```text
Medical PDF
      │
      ▼
PyPDF Loader
      │
      ▼
Text Chunking
(500 Chunk Size,
20 Overlap)
      │
      ▼
Sentence Transformers
(all-MiniLM-L6-v2)
      │
      ▼
384-Dimensional Embeddings
      │
      ▼
Pinecone Vector Database
      │
      ▼
Top-3 Similarity Retrieval
      │
      ▼
LangChain Retrieval Chain
      │
      ▼
Groq Llama-3.3-70B
      │
      ▼
Streamlit Chat Interface
```

---

## 📊 Project Statistics

| Metric | Value |
|----------|----------|
| Chunk Size | 500 |
| Chunk Overlap | 20 |
| Embedding Model | all-MiniLM-L6-v2 |
| Embedding Dimension | 384 |
| Retrieval Strategy | Similarity Search |
| Top-K Retrieval | 3 |
| Vector Database | Pinecone |
| LLM | Llama-3.3-70B |
| Framework | LangChain |
| Frontend | Streamlit |

---

## 🛠️ Tech Stack

### Generative AI

- LangChain
- Groq
- Llama-3.3-70B
- Retrieval-Augmented Generation (RAG)

### Embeddings

- HuggingFace Embeddings
- Sentence Transformers
- all-MiniLM-L6-v2

### Vector Database

- Pinecone

### Backend

- Python
- PyPDF
- dotenv

### Frontend

- Streamlit

---

## 📁 Project Structure

```text
medassist-ai/
│
├── data/
│
├── research/
│   └── trials.ipynb
│
├── src/
│   ├── __init__.py
│   ├── helper.py
│   └── prompt.py
│
├── app.py
├── store_index.py
├── requirements.txt
├── setup.py
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/bitwise-arnesh/medassist-ai.git
cd medassist-ai
```

### Create Environment

```bash
conda create -n medibot python=3.10 -y
conda activate medibot
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
PINECONE_API_KEY=your_pinecone_api_key
GROQ_API_KEY=your_groq_api_key
```

---

## 📚 Build Vector Index

```bash
python store_index.py
```

This process:

- Loads PDF documents
- Splits documents into chunks
- Generates embeddings
- Creates Pinecone index
- Stores vectors for retrieval

---

## ▶️ Run Application

```bash
streamlit run app.py
```

Application launches at:

```text
http://localhost:8501
```

---

## 💡 Example Queries

```text
What is diabetes?

What is acromegaly?

What causes hypertension?

What are the symptoms of anemia?

How is asthma treated?
```

---

## 🎯 Key Learnings

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Databases
- Embedding Models
- Similarity Search
- LangChain Retrieval Chains
- LLM Integration with Groq
- Streamlit Application Development
- End-to-End GenAI Pipeline Design

---

## 🔮 Future Improvements

- Source citations
- Chat history memory
- Multi-document support
- PDF upload through UI
- Streaming responses
- Cloud deployment
- Dockerization

---

## 👨‍💻 Author

**Arnesh Bera**

- GitHub: https://github.com/bitwise-arnesh
- LinkedIn: https://www.linkedin.com/in/arnesh-bera

---

⭐ If you found this project useful, consider giving it a star.
