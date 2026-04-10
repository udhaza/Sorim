import json
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

# Load dataset
with open("data/vehicles.json") as f:
    data = json.load(f)

chunks = []
texts = []

for vehicle in data["vehicles"]:
    text = f"""
    Model: {vehicle['model']}
    Type: {vehicle['type']}
    Seating: {vehicle['seating_capacity']}
    Engine: {vehicle['engine_specs']}
    Fuel: {vehicle['fuel_type']}
    Safety: {', '.join(vehicle['safety_features'])}

    Service:
    Oil change: {vehicle['service']['oil_change_interval']}
    Tire rotation: {vehicle['service']['tire_rotation_schedule']}
    """

    chunks.append({
        "model": vehicle["model"],
        "text": text
    })

    texts.append(text)

# Save chunks
with open("data/chunks.json", "w") as f:
    json.dump(chunks, f, indent=2)

# Create embeddings
embeddings = model.encode(texts)

# FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

faiss.write_index(index, "data/faiss_index.bin")

print(" Embeddings + FAISS index created")