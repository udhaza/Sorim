import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

index = faiss.read_index("data/faiss_index.bin")

with open("data/chunks.json") as f:
    chunks = json.load(f)


def search(query, k=3):
    query_vec = model.encode([query])
    distances, indices = index.search(np.array(query_vec), k)

    results = []
    for i in indices[0]:
        results.append(chunks[i])

    return results