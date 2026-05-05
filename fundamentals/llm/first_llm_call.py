# Demonstrates basic LLM usage for text summarization

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="gpt-4.1-mini",
    input="""
Extract the following from this text and return JSON:

- goal
- domain
- intent

Text:
I am transitioning into AI engineering and building real-world projects.
"""
)

import json

raw_output = response.output_text

# Remove markdown if present
cleaned = raw_output.replace("```json", "").replace("```", "").strip()

data = json.loads(cleaned)

print(data)
print("\nGoal:", data["goal"])