import httpx
from openai import AsyncOpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def gpt4(question):
        response = await client.chat.completions.create(
            messages=[{"role": "user", "content": str(question)}],
            model="gpt-4o",
        )
        return response
