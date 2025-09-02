# from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from config import _GOOGLE_API_KEY
from config import _GROQ_API_KEY

# llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash",api_key=_GOOGLE_API_KEY)
llm = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct",api_key=_GROQ_API_KEY)
# Simple text invocation
result = llm.invoke("tell me a one motivatinoal quote.")
print(result.content)

# Multimodal invocation with gemini-pro-vision
message = HumanMessage(
    content=[
        {
            "type": "text",
            "text": "What's in this image?",
        },
        {"type": "image_url", "image_url": "https://picsum.photos/seed/picsum/200/300"},
    ]
)
result = llm.invoke([message])
print(result.content)