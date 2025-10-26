# YouTube Summarizer Bot – Your Personal Study Assistant
<div align="center">
  <img width="640" height="360" alt="YTSummarizer" src="https://github.com/user-attachments/assets/cd9cb536-8198-488f-8936-bcb754460fc6" />
</div>

## Your personal study assistant!
Your personal study assistant! This bot makes learning easier by converting YouTube videos into summarized notes with key points. Just send a video link, and get a clear PDF summary—perfect for studying, revising, or quickly understanding any topic. Say goodbye to long videos and hello to smart learning

A demo project to study about ML models and how the models works

---

## Features

* Download YouTube audio with `yt-dlp`
*  Transcribe audio into text using **OpenAI Whisper**
*  Detect spoken language automatically
*  Translate **Malayalam → English** using **mBART**
*  Summarize long transcripts using **BART Large CNN**
*  Extract key points for quick revision
*  Generate a **PDF report** with summary + key points
*  Get results directly in Telegram

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
 ┣ 📜 main.py            # Main bot code
 ┣ 📜 requirements.txt  # Dependencies
 ┣ 📜 README.md         # Documentation
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/harikrishnan669/youtube-summarizer.git
cd youtube-summarizer
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

##  Usage

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
## Scrrenshots
<table>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/33f3e9c8-57bb-4ff2-8798-e312eb489b6a" width="200"/></td>
    <td><img src="https://github.com/user-attachments/assets/df4674b1-3496-41dc-a74e-7cb5a68bf476" width="200"/></td>
    <td><img src="https://github.com/user-attachments/assets/52b57430-34e2-4c5f-ab70-9b72132e2324" width="200"/></td>
    <td><img src="https://github.com/user-attachments/assets/3485b28f-d3b0-4820-b878-3829cc74bf6e" width="200"/></td>
  </tr>
</table>

---
## 📄 License

MIT License – Feel free to use and modify.

---
