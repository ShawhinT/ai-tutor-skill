from dotenv import load_dotenv
import os
from groq import Groq
import json

from scripts.get_youtube_transcript import (
    extract_video_id,
    get_transcript,
    format_transcript
)

load_dotenv()

with open("SKILL.md", "r", encoding="utf-8") as f:
    SKILL_TEXT = f.read()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

YOUTUBE_TOOL = {
    "type": "function",
    "function": {
        "name": "get_youtube_transcript",
        "description": "Get the transcript of a YouTube video using a URL or video ID",
        "parameters": {
            "type": "object",
            "properties": {
                "url_or_id": {
                    "type": "string",
                    "description": "YouTube video URL or video ID"
                }
            },
            "required": ["url_or_id"]
        }
    }
}

def chat():
    print("🤖 AI Tutor Skill ready. Type 'exit' to quit.\n")
    
    messages = [
        {
            "role": "system",
            "content": f"""
You are an AI tutor agent.

You have the following skill:
{SKILL_TEXT}

You also have access to a tool called `get_youtube_transcript`.

RULES:
- If the user asks about a YouTube video,
- you MUST call `get_youtube_transcript`
- NEVER guess or summarize without transcript.
"""
        }
    ]

    while True:
        user_input = input("You > ")
        if user_input.lower() == "exit":
            break

        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model="meta-llama/llama-4-maverick-17b-128e-instruct",
            messages=messages,
            tools=[YOUTUBE_TOOL],
            tool_choice="auto"
        )

        msg = response.choices[0].message

        # If the LLM requests a tool
        if msg.tool_calls:
            for call in msg.tool_calls:
                if call.function.name == "get_youtube_transcript":
                    args = json.loads(call.function.arguments)
                    url_or_id = args["url_or_id"]

                    print(f"🔍 Fetching transcript for: {url_or_id}...")
                    video_id = extract_video_id(url_or_id)
                    try:
                        transcript = get_transcript(video_id)
                        transcript_text = format_transcript(transcript)

                        # Truncate transcript to stay within token limits (approx 10k chars)
                        if len(transcript_text) > 10000:
                            transcript_text = transcript_text[:10000] + "... [Transcript truncated due to length]"
                    except Exception as e:
                        transcript_text = f"Error fetching transcript: {str(e)}"

                    # Send tool result back
                    messages.append(msg)
                    messages.append({
                        "role": "tool",
                        "tool_call_id": call.id,
                        "content": transcript_text
                    })

                    final = client.chat.completions.create(
                        model="meta-llama/llama-4-maverick-17b-128e-instruct",
                        messages=messages
                    )
                    
                    ai_response = final.choices[0].message.content
                    print("\nAI >", ai_response, "\n")
                    messages.append({"role": "assistant", "content": ai_response})
        else:
            print("\nAI >", msg.content, "\n")
            messages.append({"role": "assistant", "content": msg.content})

if __name__ == "__main__":
    chat()
