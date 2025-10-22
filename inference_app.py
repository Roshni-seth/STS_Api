# inference_app.py
from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer, util
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Semantic Textual Similarity API",
    description="Returns semantic similarity score between two text paragraphs (0–1 scale)",
    version="1.0"
)

# Load pre-trained lightweight model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

class TextPair(BaseModel):
    text1: str
    text2: str

# POST endpoint: always returns JSON in your required format
@app.post("/", tags=["Similarity"])
def get_similarity(data: TextPair):
    emb1 = model.encode(data.text1, convert_to_tensor=True)
    emb2 = model.encode(data.text2, convert_to_tensor=True)
    similarity = util.cos_sim(emb1, emb2).item()
    normalized_score = (similarity + 1) / 2
    return JSONResponse(content={
        "text1": data.text1,
        "text2": data.text2,
        "similarity score": round(normalized_score, 4)
    })

# GET endpoint for browser
@app.get("/", tags=["Home"])
def home():
    return JSONResponse(content={
        "message": "Welcome to the Semantic Text Similarity API. Use POST requests with text1 and text2."
    })
