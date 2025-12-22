from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()

with open("SKILL.md", "r", encoding="utf-8") as f:
    SKILL_TEXT = f.read()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def chat():
    print("🤖 AI Tutor Skill ready. Type 'exit' to quit.\n")

    while True:
        user_input = input("You > ")
        if user_input.lower() == "exit":
            break

        messages = [
            {
                "role": "system",
                "content": f"You have the following skill:\n\n{SKILL_TEXT}"
            },
            {"role": "user", "content": user_input}
        ]

        response = client.chat.completions.create(
            model="meta-llama/llama-4-maverick-17b-128e-instruct",
            messages=messages # type: ignore
        )

        print("\nAI >", response.choices[0].message.content, "\n")

if __name__ == "__main__":
    chat()
