from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI()

# Enable CORS to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (you can restrict this later)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Hugging Face API details
HF_API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
HF_HEADERS = {"Authorization": "Bearer YOUR_HUGGINGFACE_API_KEY"}  # Replace with your Hugging Face API key

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(request: ChatRequest):
    user_message = request.message

    # Sending request to Hugging Face API
    response = requests.post(HF_API_URL, headers=HF_HEADERS, json={"inputs": user_message})

    if response.status_code == 200:
        bot_reply = response.json()[0]["generated_text"]
    else:
        bot_reply = "Sorry, I am having trouble responding right now."

    return {"response": bot_reply}
