import os
from together import Together
from dotenv import load_dotenv

load_dotenv()

print(os.environ.get('TOGETHER_API_KEY'))
client = Together(api_key=os.environ.get('TOGETHER_API_KEY'))

stream = client.chat.completions.create(
    model="meta-llama/Llama-3-8b-chat-hf",
    messages=[],
    max_tokens=512,
    temperature=0.7,
    top_p=0.7,
    top_k=50,
    repetition_penalty=1,
    stop=["<|eot_id|>"],
    stream=True
)

for chunk in stream:
  print(chunk.choices[0].delta.content or "", end="", flush=True)