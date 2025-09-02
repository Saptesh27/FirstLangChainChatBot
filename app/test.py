import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise RuntimeError("GOOGLE_API_KEY not found. Did you set it in .env?")


llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", api_key=api_key)

# Simple text call
result = llm.invoke("Write me a short motivational quote.")
print(result.content)