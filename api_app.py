# api_app.py
import gradio as gr
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def predict(text1, text2):
    emb1 = model.encode(text1, convert_to_tensor=True)
    emb2 = model.encode(text2, convert_to_tensor=True)
    similarity = util.cos_sim(emb1, emb2).item()
    normalized_score = (similarity + 1) / 2
    return {"similarity score": round(normalized_score, 4)}

iface = gr.Interface(
    fn=predict,
    inputs=["text", "text"],
    outputs="json",
    live=False
)

iface.launch()
