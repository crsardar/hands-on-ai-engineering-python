import os
import tiktoken
from dotenv import load_dotenv
from openai import OpenAI
from openai.types.shared_params import reasoning_effort

# gpt-6-luna isn't in tiktoken yet, so we use the encoding of recent OpenAI models
encoding = tiktoken.get_encoding("o200k_base")

tokens = encoding.encode("Hi my name is Chitta, I love chicken curry.")
for token_id in tokens:
    token_text = encoding.decode([token_id])
    print(f"{token_id} = {token_text}")

load_dotenv(override=True)
openapi_key = os.getenv("OPENAI_API_KEY")

openai = OpenAI(api_key=openapi_key)
prompts = [
    {
        "role": "system",
        "content": "You are a helpful assistant"
    },
    {
        "role": "user",
        "content": "My name is Chitta"
    }
]
response = openai.chat.completions.create(model="gpt-6-luna", reasoning_effort="none", messages=prompts)
print(response.choices[0].message.content)

prompts = [
    {
        "role": "system",
        "content": "You are a helpful assistant"
    },
    {
        "role": "user",
        "content": "What's my name?"
    }
]
response = openai.chat.completions.create(model="gpt-6-luna", reasoning_effort="none", messages=prompts)
print(response.choices[0].message.content)

prompts = [
    {
        "role": "system",
        "content": "You are a helpful assistant"
    },
    {
        "role": "user",
        "content": "Hi! I'm Chitta!"
    },
    {
        "role": "assistant",
        "content": "Hi Chitta! How can I assist you today?"
    },
    {
        "role": "user",
        "content": "What's my name?"
    }
]

response = openai.chat.completions.create(model="gpt-6-luna", messages=prompts)
print(response.choices[0].message.content)