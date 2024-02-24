# RAG for PDF

This repository contains an implementation of the Retrieval-Augmented Generation (RAG) model tailored for PDF documents. The RAG model enhances the traditional sequence-to-sequence models by incorporating a retriever component, allowing it to retrieve relevant information from a large knowledge base before generating responses.

## Overview

The RAG for PDF project aims to leverage state-of-the-art natural language processing techniques to enhance the process of reading and extracting information from PDF documents. It utilizes the following components:

- **PDF Reader and Parser**: Utilizing PDF Reader, the system parses PDF documents to extract relevant passages that serve as the knowledge base for the Embedding model.
- **Embedding Model** : Utilizing Embedding Model to Embedd the Data Parsed from PDF to be stored in VectorStore For Further Use as well as the Query Embedding for the Similarity Search by Vector Database FAISS.

- **OpenAI Chatbot Model**: Integrated with the Embedding model, the OpenAI Chatbot model facilitates interaction by understanding and generating human-like responses to queries.

- **FAISS for Vector Database**: FAISS (Facebook AI Similarity Search) is employed to efficiently store and retrieve vector representations of text passages, enabling fast and scalable retrieval for the RAG model  with LangChain used as Wrappers

## Features

- **Interactive Querying**: Users can interactively query the system with natural language questions or prompts related to the content of PDF documents.

- **Contextual Responses**: The system provides responses that are contextually relevant, thanks to the retrieval of passages from PDF documents.

- **Scalability**: Utilizing FAISS for vector storage allows for efficient scaling, enabling the system to handle large collections of PDF documents.

-  **Lanchain**: Lanchain is utilized for secure and efficient communication between components of the system, ensuring data privacy and integrity.

## Getting Started

To get started with using the RAG for PDF system, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/AkshayPethe/RAG_for_PDF.git

2.Install the necessary dependencies:
pip install -r requirements.txt

3.Run Application:
streamlit run app.py

#### Feel free to use and modify this README file according to your requirements! If you have any further questions or need additional assistance, please let me know.
