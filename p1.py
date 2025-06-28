from groq import Groq
import os

client = Groq(api_key=os.environ["GROQ_API_KEY"])

response = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[{"role": "user", "content": "Explain transformers in AI"}]
)

print(response.choices[0].message.content)