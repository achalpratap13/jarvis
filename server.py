from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Query(BaseModel):
    text: str
    device: str

@app.post("/ask")
def ask(query: Query):
    if "chrome" in query.text.lower():
        reply = "ठीक है, मैं Chrome खोल रहा हूँ।"
    else:
        reply = f"आपने कहा: {query.text}"
    return {"reply": reply}
