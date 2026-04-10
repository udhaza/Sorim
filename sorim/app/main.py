from fastapi import FastAPI
from app.search import search
from app.rag import generate_answer
from app.recommend import recommend

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/search")
def search_api(q: str):
    return search(q)


@app.get("/ask")
def ask_api(q: str):
    return generate_answer(q)


@app.get("/recommend")
def recommend_api(q: str):
    return recommend(q)