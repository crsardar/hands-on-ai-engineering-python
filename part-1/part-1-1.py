import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

if not api_key:
    print("API Key NOT found")
elif not api_key.startswith("sk-proj-"):
    print("API Key FOUND. But it doesn't start sk-proj-; please check you're using the right key.")
elif api_key.strip() != api_key:
    print("API Key FOUND. But is is EMPTY.")
else:
    print("API Key FOUND. And looks good so far!")
message = "Hello, GPT! This is my first ever message to you! Hi!"

prompts = [{"role": "user", "content": message}]

openai = OpenAI(api_key=api_key)
response = openai.chat.completions.create(model="gpt-5.4-mini", messages=prompts)
print(response.choices[0].message.content)
