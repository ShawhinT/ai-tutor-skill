# Project Understanding: AI Tutor Skill

This document explains how this project works, using the very same "Skill Concepts" the AI Tutor uses to teach you.

## What is a "Skill"? (What → Why → How)

### What
A **Skill** is a set of specialized instructions and "mental models" stored in a Markdown file (`SKILL.md`). It acts as the "brain" or "personality" of the AI, telling it exactly how to think and respond.

### Why
Standard AI models are generalists. By using a Skill, we force the AI to follow a specific **Teaching Framework** (like "Status Quo → Problem → Solution") instead of just giving generic answers. This makes the AI a much more effective tutor.

### How
1. **Loading**: The `chat.py` script reads the text inside `SKILL.md`.
2. **Injection**: It injects that text into the **System Prompt** of every API call to Groq.
3. **Execution**: The LLM (Llama 3) reads those instructions first and uses them to structure its response to your questions.

---

## Project Architecture (The "So What")

Here is how the different files in your folder work together:

| File | Role | So What? |
| :--- | :--- | :--- |
| `SKILL.md` | **The Teacher's Manual** | Defines the narrative structures (e.g., Status Quo → Problem → Solution). |
| `chat.py` | **The Engine** | Connects you to the AI, manages the conversation history, and handles tool calls. |
| `scripts/get_youtube_transcript.py` | **The Researcher** | A specialized tool that goes to YouTube, grabs the text of a video, and brings it back. |
| `.env` | **The Keyring** | Stores your `GROQ_API_KEY` securely so the script can talk to the AI. |

---

## The Workflow (Status Quo → Problem → Solution)

### Status Quo
You have a technical question or a YouTube video you don't have time to watch.

### Problem
Technical concepts are often buried in jargon or long videos, making them hard to digest quickly.

### Solution
1. You ask a question in `chat.py`.
2. If you provide a link, the AI triggers the `get_youtube_transcript` tool.
3. The script fetches the transcript, truncates it to fit the model's memory, and feeds it to the AI.
4. The AI applies the **Teaching Principles** (Plain English, Concrete Examples) from your `SKILL.md` to give you a structured, easy-to-understand summary.

---

## Key Concepts to Remember

*   **System Prompt**: This is the "hidden" instruction that tells the AI "You are an AI Tutor."
*   **Tool Calling**: The AI doesn't just "know" what's in a video; it has to "decide" to run the Python script to get that data.
*   **Token Limits**: Models have a "memory limit" (6,000 tokens for this model). This is why we truncate long transcripts in `chat.py`.
