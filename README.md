# AI Tutor Skill

A **universal AI tutor** that explains complex technical concepts (AI, ML, and beyond) in accessible, plain English. This project uses **Skill Concepts**—structured narrative frameworks—to transform abstract ideas into clear, teachable explanations.

**Works with any LLM** (Groq, OpenAI, Claude, Llama, etc.)—not limited to Claude Code.

---

## 🍴 About This Fork

**Original Project**: [ShawinT/ai-tutor-skill](https://github.com/ShawinT/ai-tutor-skill)

**What's New in This Fork:**
- ✅ Fixed YouTube transcript token overflow (smart 10k char truncation)
- ✅ Added multi-turn conversation loop (ask multiple questions)
- ✅ Better error handling for transcript failures
- ✅ Works with **any LLM** (Groq, OpenAI, Anthropic, etc.)
- ✅ Beginner-friendly README with clear contribution steps

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

## 🛠️ Advanced: Use Different LLMs

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

---

## ❓ FAQ

**Q: I'm scared I'll break something**
A: You won't! GitHub has full version history. Worst case, your PR gets rejected and that's fine—you learn something.

**Q: Do I need permission to contribute?**
A: Nope! That's the beauty of open source. Fork → Change → PR = Contribute.

**Q: What if my PR isn't accepted?**
A: Totally normal. Ask why, learn from feedback, try again. Every contributor has been rejected before!

**Q: Can I contribute if I don't code much?**
A: YES! You can improve docs, add examples, fix typos, etc. All valuable!

**Q: How long does PR review take?**
A: Could be hours, days, or weeks. Maintainers volunteer their time.

---

## 📖 Resources

- [Git/GitHub Guide](https://docs.github.com/en/get-started)
- [How to Make Your First Pull Request](https://www.freecodecamp.org/news/how-to-make-your-first-pull-request-on-github/)
- [Open Source 101](https://opensource.guide/)

---

## 📝 License

This project is open source. Check the LICENSE file for details.

---

**Questions?** Create an issue on GitHub or ask in the discussions. The community is here to help! 🚀
