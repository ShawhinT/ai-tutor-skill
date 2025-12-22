# AI Tutor Skill

A **universal AI tutor** that explains complex technical concepts (AI, ML, and beyond) in accessible, plain English. This project uses **Skill Concepts**—structured narrative frameworks—to transform abstract ideas into clear, teachable explanations.

**Works with any LLM** (Groq, OpenAI, Claude, Llama, etc.)—not limited to Claude Code.

> 🍴 **Fork Info**: This is an enhanced fork of [ShawinT/ai-tutor-skill](https://github.com/ShawinT/ai-tutor-skill)
> 
> **Improvements in this fork:**
> - ✨ Fixed YouTube transcript token overflow issue (smart truncation to 10k chars)
> - ✨ Added persistent conversation loop (multi-turn chatting)
> - ✨ Enhanced error handling for transcript fetching failures
> - ✨ Made LLM-agnostic (works with any provider, not just Claude)
> - ✨ Comprehensive README with contributor guidelines
> - ✨ Project understanding guide for newcomers

## Resources

- [YouTube Explainer: Claude Skills](https://youtu.be/vEvytl7wrGM)
- [See Understanding Guide](#project-understanding) below

## Quick Start

### Requirements

- **Python**: >= 3.12
- **Package Manager**: [uv](https://github.com/astral-sh/uv)
- **API Key**: Get a free key from [Groq Console](https://console.groq.com)

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd ai-tutor-skill
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```

3. Create a `.env` file in the root directory:
   ```env
   GROQ_API_KEY=your_api_key_here
   ```

4. Run the tutor:
   ```bash
   uv run python chat.py
   ```

## Project Understanding

### What is a "Skill"?

A **Skill** is a set of specialized instructions stored in a Markdown file (`SKILL.md`). It acts as the "brain" or "personality" of the AI, telling it exactly how to think and respond.

**Why use Skills?**
- Standard AI models are generalists and give generic answers.
- Skills enforce a specific **Teaching Framework** (e.g., "Status Quo → Problem → Solution") for consistent, effective explanations.
- Same skill can be used with any LLM provider.

### How It Works (Status Quo → Problem → Solution)

**Status Quo:**
You have a technical question or a YouTube video you don't have time to watch.

**Problem:**
Technical concepts are buried in jargon or long videos, making them hard to digest quickly.

**Solution:**
1. You ask a question in `chat.py`
2. If you provide a YouTube link, the AI calls the `get_youtube_transcript` tool
3. The script fetches the transcript, truncates it to fit the model's memory (token limits)
4. The AI applies **Teaching Principles** from `SKILL.md` to give you a structured summary

### Project Architecture

| File | Role |
| :--- | :--- |
| `SKILL.md` | **The Teacher's Manual**—defines narrative structures and teaching principles |
| `chat.py` | **The Engine**—connects you to the AI, manages conversation history, handles tool calls |
| `scripts/get_youtube_transcript.py` | **The Researcher**—fetches YouTube transcripts |
| `.env` | **The Keyring**—stores your API key securely |

### Key Concepts

- **System Prompt**: Hidden instruction that tells the AI "You are an AI Tutor" and injects the skill
- **Tool Calling**: The AI decides when to use the YouTube transcript tool
- **Token Limits**: Models have memory constraints (~6,000 tokens). Transcripts from videos longer than ~15 minutes will be truncated

---

## Contributing

### For Developers

This project is designed to be **accessible and extensible**:

1. **Add New Narrative Frameworks**: Edit `SKILL.md` to add teaching structures beyond "Status Quo → Problem → Solution"
2. **Add New Tools**: Extend `chat.py` to support new data sources (research papers, documentation, etc.)
3. **Switch LLM Providers**: Change the API client in `chat.py` (currently uses Groq, but can use OpenAI, Anthropic, etc.)
4. **Improve Teaching Logic**: Enhance the AI tutor's behavior by refining the system prompt

### Using Different LLMs

To use a different LLM provider instead of Groq:

1. Install the provider's SDK (e.g., `openai`, `anthropic`)
2. Modify `chat.py` to replace the Groq client with your provider's client
3. Update the model name (e.g., `gpt-4`, `claude-3-sonnet`)

Example for OpenAI:
```python
from openai import OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Then use: model="gpt-4"
```

### YouTube Transcript Note

YouTube transcript extraction works with any LLM running locally. Cloud-based AI assistants (like Claude Code in remote mode) may face blocking, but this local Python script has no such restrictions.

---

## Roadmap

- [ ] Support for research paper extraction
- [ ] Support for documentation APIs (ReadTheDocs, etc.)
- [ ] Multi-turn conversation history visualization
- [ ] Custom skill template generator
- [ ] Support for non-English teaching frameworks
