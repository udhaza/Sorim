import requests
from app.search import search

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_answer(query):
    print("\n Received Query:", query)   #1. Check request coming

    results = search(query, k=3)
    print(" Search Results:", results)   #2. Check FAISS working

    if not results:
        return {"answer": "No relevant vehicle information found."}

    # Build context
    context = "\n\n".join([r["text"] for r in results])
    print(" Context Sent to LLM:\n", context)   #3. Check context

    prompt = f"""
You are an automotive assistant.

STRICT RULES:
- Answer ONLY using the context below
- Do NOT add extra knowledge
- If answer is not in context, say "Information not available in dataset"

Context:
{context}

Question:
{query}

Answer:
"""

    try:
        print("Calling Ollama API...")   #4. Check API call

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )

        print("Raw Response:", response.text)   #5. See raw output

        result = response.json()
        answer = result.get("response", "").strip()

        print("Final Answer:", answer)   #6. Final output

        return {"answer": answer}

    except Exception as e:
        print("ERROR:", str(e))   #7. Catch failures
        return {"answer": f"Error connecting to LLM: {str(e)}"}
