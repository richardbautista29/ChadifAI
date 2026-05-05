# Demonstrates basic LLM usage for text summarization

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI()

text = """
I am transitioning into AI engineering and building real-world projects
to strengthen my skills in LLM-based applications.
"""

response = client.responses.create(
    model="gpt-4.1-mini",
    input=f"Summarize this:\n{text}"
)

print(response.output_text)