import os
from openai import OpenAI

# -----------------------------
# Load OpenAI API Key
# -----------------------------
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found")

client = OpenAI(api_key=api_key)

# -----------------------------
# Define model and initial conversation
# -----------------------------
model = "gpt-4o-mini"

conversation = [
    {"role": "system", "content": "You are a concise travel guide for Paris."},
    {"role": "user", "content": "What is the most famous landmark in Paris?"},
    {"role": "assistant", "content": "The most famous landmark in Paris is the Eiffel Tower."}
]

# -----------------------------
# List of questions
# -----------------------------
questions = [
    "How far away is the Louvre from the Eiffel Tower?",
    "Where is the Arc de Triomphe?",
    "What are the must-see artworks at the Louvre Museum?"
]