Automotive AI Knowledge Assistant
Overview

This project is a Mini AI-powered automotive assistant that answers vehicle-related queries using:

Semantic Search (FAISS)
Retrieval-Augmented Generation (RAG)
Rule-based Recommendation System

Features:
    Search vehicle data using semantic similarity
    Ask questions using RAG + local LLM (LLaMA3 via Ollama)
    Get vehicle recommendations
    Simple UI for interaction

Setup Instructions:

1. Clone the Repository 
    git clone 

2. Create Virtual Environment
    python -m venv venv
    venv\Scripts\Activate

3. Install Dependencies
    pip install -r  requirements.txt

4.Generate Embeddings
    python app/embedding.py

5. Start Local LLM (Ollama)
    ollama run llama3

6. Run FastAPI Server
    python uvicorn app.main:app --reload --port 8001

7.Access Application
    API Docs: http://127.0.0.1:8001/docs
    Frontend UI: Open frontend/index.html

Architecture Explanation:

Components:

1. Semantic Search
    Converts query into embeddings
    Uses FAISS for similarity search
    Retrieves most relevant vehicle data

2. RAG Assistant (Retrieval-Augmentated Generator)
    Retreival - FAISS 
    Generation - LLM

    Process:
    1. Retreive relevant data chunks
    2. Inject into prompt
    3. Generate grounded answer using LLama3

    -Prevents hallucination
    -Ensures accuracy
    -Uses only dataset information

3. Recommendation Engine
    Rule-based scoring system
    Matches:
    Vehicle type
    Seating capacity
    Fuel type
    User intent (family, towing, etc.)
    Returns top 2 vehicles with explanation

Design Decisions

1.JSON Dataset:
    Structures and easy to process
    Supports both RAG and Filtering

2.FAISS for Semantic Search:
    Fast similarity search
    Efficient for large datasets
    Works well with embeddings

3.Sentence Transformers
    Converts text to Embeddings
    Captures Semantic meaning 

4.RAG for Answer Generation
    Combines retrieval + generation
    Prevents hallucination
    Ensures domain-specific accuracy

5.Ollama (Local LLM)
    Free and runs locally
    No API cost
    Enables real LLM-based responses
    
6.Rule-Based Recommendation
    Transparent and explainable
    Easy to debug
    Matches assignment requirement (logical filtering)

7.Chunking Strategy
    Data split into meaningful sections:
        Vehicle specs
        Service info
        Manual content
    Improves retrieval accuracy