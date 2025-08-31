# YouTube Summarizer Telegram Bot

An **AI-powered Telegram bot** that converts YouTube videos into concise **summaries + key points in PDF**.
It works for both **English** and **Malayalam** videos 🎧📑.

---

## Features

* 📥 Download YouTube audio with `yt-dlp`
* 📝 Transcribe audio into text using **OpenAI Whisper**
* 🌐 Detect spoken language automatically
* 🌍 Translate **Malayalam → English** using **mBART**
* 📖 Summarize long transcripts using **BART Large CNN**
* 📌 Extract key points for quick revision
* 📄 Generate a **PDF report** with summary + key points
* 🤖 Get results directly in Telegram

---

## Models Used

### 1. **Whisper (Base Model)**

* Source: [OpenAI Whisper](https://github.com/openai/whisper)
* Task: **Speech-to-text transcription** and **language detection**
* Strength: Works with noisy audio and supports multiple languages.

### 2. **facebook/bart-large-cnn**

* Source: [Hugging Face BART](https://huggingface.co/facebook/bart-large-cnn)
* Task: **Summarization of English text**
* Strength: Extracts concise, human-readable summaries from long transcripts.

### 3. **facebook/mbart-large-50-many-to-many-mmt**

* Source: [Hugging Face mBART](https://huggingface.co/facebook/mbart-large-50-many-to-many-mmt)
* Task: **Translation (Malayalam → English)**
* Strength: Supports **50 languages**, making the bot multilingual.

---

## ⚡ Workflow

### Step-by-step Flow:

1. **User sends YouTube link** in Telegram
2. **Bot downloads audio** using `yt-dlp`
3. **Whisper transcribes audio** → Returns full transcript
4. **Language detection**:

   * If English → move to summarization
   * If Malayalam → Translate Malayalam → English using mBART
5. **Summarize transcript** with **BART-Large-CNN**
6. **Extract key points** (max 8 important sentences)
7. **Generate PDF** with:

   * Title
   * Summary
   * Key points
   * Footer (Bot signature)
8. **Bot sends back results**:

   * Summary in text format
   * PDF file with key points

---

## Flow Diagram
<img width="500" height="800" alt="ChatGPT Image Aug 31, 2025, 08_41_55 PM" src="https://github.com/user-attachments/assets/db096434-c7c1-4ebb-b3e1-ddb6364f68cf" />

## File Structure
```
📦 youtube-summarizer-bot
 ┣ 📜 bot.py            # Main bot code
 ┣ 📜 requirements.txt  # Dependencies
 ┣ 📜 README.md         # Documentation
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/youtube-summarizer-bot.git
cd youtube-summarizer-bot
```

### 2. Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**requirements.txt**

```txt
python-telegram-bot==20.3
transformers==4.31.0
torch
yt-dlp
openai-whisper
fpdf
```

### 4. Add Your Bot Token

* Get a bot token from **BotFather** on Telegram.
* Open `bot.py` and replace:

```python
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
```

### 5. Run the Bot

```bash
python bot.py
```

---

## 🤖 Usage

* Start the bot in Telegram: `/start`
* Send a YouTube link 🎥
* Bot replies with:

  * 📄 A **text summary** (Telegram message)
  * 📑 A **PDF report** with key points

---

## 📜 Commands

| Command  | Description                  |
| -------- | ---------------------------- |
| `/start` | Start the bot                |
| `/help`  | Show available commands      |
| `/steps` | Show bot workflow steps      |
| `/clear` | Clear session (experimental) |

---

## 📌 Example Output

**Summary (Telegram Message):**

```
This video explains the basics of AI, its applications in daily life, and future challenges...
```

**PDF Key Points:**

* AI is transforming industries
* Applications include healthcare, finance, education
* Challenges include ethics & privacy

---

## 🚀 Future Improvements

* 📊 Better PDF formatting (colors, sections, headings)
* 🌍 Support for more languages
* ☁️ Cloud storage for generated PDFs
* 🎥 Handle **very long videos** with chunk-based transcript summarization

---

## 🤝 Contributing

Pull requests are welcome! Please open an issue first to discuss major changes.

---

## 📄 License

MIT License – Feel free to use and modify.

---
