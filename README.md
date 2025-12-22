# AI Tutor Skill

A **universal AI tutor** that explains complex technical concepts (AI, ML, and beyond) in accessible, plain English. This project uses **Skill Concepts**—structured narrative frameworks—to transform abstract ideas into clear, teachable explanations.

**Works with any LLM** (Groq, OpenAI, Claude, Llama, etc.)—not limited to Claude Code.

---

## 🍴 About This Fork

**Original Project**: [ShawinT/ai-tutor-skill](https://github.com/ShawinT/ai-tutor-skill)

**What's New in This Fork:**
- ✅ Fixed YouTube transcript token overflow for Groq's 6k TPM limit (smart 10k char truncation)
- ✅ Added multi-turn conversation loop (ask multiple questions)
- ✅ Better error handling for transcript failures
- ✅ Works with **any LLM** (Groq, OpenAI, Anthropic, etc.)
- ✅ Beginner-friendly README with clear documentation

---

## ⚡ Quick Start (5 Minutes)

### 1. Install Requirements
- **Python** 3.12+
- **uv** package manager ([Install here](https://github.com/astral-sh/uv))
- **Groq API Key** (free, [get it here](https://console.groq.com))

### 2. Setup
```bash
# Clone this repo
git clone https://github.com/yourusername/ai-tutor-skill.git
cd ai-tutor-skill

# Install dependencies
uv sync

# Create .env file with your API key
echo "GROQ_API_KEY=your_key_here" > .env
```

### 3. Run It
```bash
uv run python chat.py
```

**Example:**
```
🤖 AI Tutor Skill ready. Type 'exit' to quit.

You > hi

AI > Hello! I'm here to help explain technical concepts in a clear and accessible way. What would you like to learn about or understand better?

You > explain me machine learning?

AI > Let's break down machine learning into a clear explanation.

Machine learning is a way to make computers learn from data, so they can make predictions or decisions without being explicitly programmed.

### Status Quo → Problem → Solution

1. **Status Quo**: Traditionally, computers were programmed with rules to perform specific tasks. For example, a spam filter might be programmed with rules like "if the email contains the word 'free', it's likely spam."
2. **Problem**: As data grows, it becomes impractical to write rules for every possible scenario. For instance, predicting whether a customer will churn or not based on their behavior is complex and can't be captured by simple rules.
3. **Solution**: Machine learning allows computers to learn patterns from data, so they can make predictions or decisions. In the case of the customer churn prediction, a machine learning model can be trained on historical data to identify patterns that indicate a customer is likely to churn.

### Concrete Example

Let's consider a simple example: building a machine learning model to predict house prices based on features like the number of bedrooms, square footage, and location.

1. **Data Collection**: We gather data on past house sales, including their prices and features.
2. **Data Preprocessing**: We clean the data, handle missing values, and normalize features.
3. **Model Selection**: We choose a regression algorithm (like linear regression or a more complex model like a random forest) based on the data and problem.
4. **Training**: We train the model on the historical data, allowing it to learn the relationship between house features and prices.
5. **Evaluation**: We test the model on new data to see how accurately it predicts house prices.

You > explain this youtube video? https://youtu.be/vEvytl7wrGM?si=RE_R4b49z9sxfJJw
🔍 Fetching transcript for: https://youtu.be/vEvytl7wrGM?si=RE_R4b49z9sxfJJw...

AI > The YouTube video explains Claude's new "Skills" feature, which allows users to provide reusable instructions to Claude, an AI model. Here's a breakdown of the key points:

### What are Claude Skills?

* Skills are reusable instructions that Claude can access when needed.
* They can be thought of as specialized prompts or workflows that Claude can follow.

### Why are Skills useful?

* They streamline the process of providing instructions to Claude, eliminating the need to manually write or copy-paste instructions every time.
* They enable Claude to automatically select the most relevant skill based on the conversation context.

### How do Skills work?

1. **Skill Structure**: A skill is essentially a folder containing a `skill.md` file, which has two main components:
   * Metadata (name and description)
   * Body (the instructions themselves)
2. **Progressive Disclosure**: Claude uses a progressive disclosure approach, where only the metadata is initially added to the context window. The body is only loaded when the skill is deemed relevant.

### Key Benefits

* **Better Context Management**: Skills allow Claude to manage context more efficiently, without sacrificing capabilities.
* **Flexibility**: Skills can be used to provide specialized instructions, tools, and workflows to Claude.

You > exit
```

---

## 📚 How This Project Works

### The Core Concept: "Skills"

A **Skill** is a set of teaching instructions (`SKILL.md`) that tells the AI:
- HOW to explain concepts (using frameworks like "Status Quo → Problem → Solution")
- WHAT principles to follow (Plain English, Concrete Examples, etc.)
- WHEN to use tools (like fetching YouTube transcripts)

Think of it as the AI's "personality" or "teaching manual."

### Project Structure

```
ai-tutor-skill/
├── SKILL.md                          # Teaching instructions (the AI's brain)
├── chat.py                           # Main app (talks to the AI)
├── scripts/
│   └── get_youtube_transcript.py     # Tool to fetch YouTube transcripts
├── .env                              # Your API key (create this)
└── pyproject.toml                    # Python dependencies
```

### How It Works Step-by-Step

1. **You ask a question** → `chat.py` receives it
2. **System injects the Skill** → Skill.md gets added to the AI's system prompt
3. **AI thinks** → Uses the teaching frameworks from Skill.md
4. **If you mention a video** → AI calls `get_youtube_transcript.py` tool
5. **Transcript is truncated** → Kept under 10k chars to fit token limits
6. **AI responds** → With a structured, easy-to-understand answer
7. **Loop** → You can ask more questions (multi-turn chat)

### Key Files Explained

| File | What It Does |
|------|------------|
| **SKILL.md** | Defines 3 teaching frameworks: "Status Quo → Problem → Solution", "What → Why → How", "What → So What → What Now" |
| **chat.py** | Connects you to Groq's LLM, manages conversation history, calls the YouTube tool |
| **scripts/get_youtube_transcript.py** | Fetches and formats YouTube video transcripts |
| **.env** | Stores your `GROQ_API_KEY` (never commit this!) |

---

## � How to Use YouTube Videos

### ✅ What Works (Direct URL)
```
You > explain this youtube video? https://youtu.be/RveLjcNl0ds?si=PbLLM-_kND9Fifq5
🔍 Fetching transcript for: https://youtu.be/RveLjcNl0ds?si=PbLLM-_kND9Fifq5...

AI > The YouTube video by Shaw Talebi discusses the recent advancements in reasoning models trained through reinforcement learning, particularly focusing on OpenAI's o1 model and DeepSeek's R1 model. Here's a breakdown of the key points:

## Background
1. OpenAI released the o1 model in September 2024, which demonstrated advanced reasoning capabilities through large-scale reinforcement learning.
2. The o1 model introduced a novel approach called "test-time compute scaling," where the model's performance improves with the number of tokens it generates during inference.

## Key Insights
- The o1 model's responses include a "thinking" phase before providing the final answer
- Performance improves as it generates more tokens ("test-time compute scaling")
- OpenAI used special "thinking tokens" to delimit the model's chain of thought

[...AI provides full explanation...]
```

### ❌ What Doesn't Work (Video Title/Search)
```
You > find a youtube video by shaw talebi on this and explain it. it might be called how to train LLMs to think?
🔍 Fetching transcript for: shaw talebi how to train LLMs to think...

AI > It seems the video wasn't found directly. Let's try a more specific search.

[Error: get_youtube_transcript failed. Please provide a valid YouTube video URL or ID...]
```

### Why?
The transcript tool **needs a direct YouTube URL or video ID**, not a search query. It cannot search YouTube.

**How to fix it:**
1. Search YouTube for the video title
2. Copy the video URL from your browser
3. Paste it into your message: `"Explain this: [URL]"`

### The Limitation I Found

I discovered that **direct YouTube URLs work, but searching by title doesn't**. The transcript tool can only extract transcripts from direct video links—it can't search YouTube like Claude Code does.

When I tried asking the AI to find a video by title, it attempted to use the tool with just text, which failed. But when I gave it a direct link, it worked perfectly.

**Note on Token Limits:** The transcript truncation (10k chars) is specifically for Groq's on-demand tier which has a 6,000 tokens per minute limit. If you switch to OpenAI or other APIs with higher limits, you can remove or increase this limit in `chat.py`.

### Why This Happens

Claude Code (web version) has built-in web search, so it can find videos automatically. This local version is simpler—it focuses on analyzing transcripts from direct links, not searching.

**Could this be improved?** Yes. I could add:
- DuckDuckGo API for searching
- Bing Web Search API  
- Custom YouTube search integration

But for now, keeping it focused on direct transcript analysis keeps things fast and simple.

---

## �🛠️ Advanced: Use Different LLMs

This project works with **any LLM**, not just Groq:

### Switch to OpenAI (GPT-4)
1. Install: `uv pip install openai`
2. Edit `chat.py`:
```python
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Change model name in API calls:
# FROM: model="meta-llama/llama-4-maverick-17b-128e-instruct"
# TO:   model="gpt-4"
```
3. Update `.env`:
```env
OPENAI_API_KEY=your_key_here
```

### Switch to Anthropic (Claude)
1. Install: `uv pip install anthropic`
2. Similar changes to `chat.py` with Anthropic client
3. Update `.env` with `ANTHROPIC_API_KEY`


## 📖 Resources

**Inspiration & Learning:**
- [Claude Skills Explained (23 min)](https://youtu.be/vEvytl7wrGM) - by Shaw Talebi - **This project is an improved, production-ready version implementing the concepts from this video!**

**Development & Contributing:**
- [Git/GitHub Guide](https://docs.github.com/en/get-started)
- [How to Make Your First Pull Request](https://www.freecodecamp.org/news/how-to-make-your-first-pull-request-on-github/)
- [Open Source 101](https://opensource.guide/)

---

## 📝 License

This project is open source. Check the LICENSE file for details.

---

