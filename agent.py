## first agent

from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
start = Groq(api_key= os.getenv("GROQ_API_KEY"))


response = start.chat.completions.create(
    model ="llama3-70b-8192",
    messages=[
        {"role" : "user", "content":"tell about today's Weather in lahore"}
    ]

)

print(response.choices[0].message.content)