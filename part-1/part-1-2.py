import os
from dotenv import load_dotenv
import requests
from openai import OpenAI

load_dotenv(override=True)
api_key = os.getenv("OPENAI_API_KEY")

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}
payload = {
    "model": "gpt-5.4-mini",
    "reasoning_effort": "none",
    "messages":[
        {
            "role":"user",
            "content":"Tell me a fun fact. But not the Octopuses"
         }
    ]
}

response = requests.post(
    "https://api.openai.com/v1/chat/completions",
    headers=headers,
    json=payload
)
print("From OpenAI >>> " + response.json()["choices"][0]["message"]["content"])


# Gemini call from OpenAI Client Library
GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
google_api_key = os.getenv("GOOGLE_API_KEY")
gemini = OpenAI(base_url=GEMINI_BASE_URL, api_key=google_api_key)
response = gemini.chat.completions.create(model="gemini-3.1-flash-lite", messages=[{"role": "user", "content": "Tell me a fun fact"}])
print("From Gemini >>> " + response.choices[0].message.content)


#  Ollama call from OpenAI Client Library
# Download/Install model to Ollama
#  !ollama pull llama3.2
OLLAMA_BASE_URL = "http://localhost:11434/v1"
ollama = OpenAI(base_url=OLLAMA_BASE_URL, api_key='ollama')
response = ollama.chat.completions.create(model="llama3.2", messages=[{"role": "user", "content": "Tell me a fun fact"}])
print(response.choices[0].message.content)