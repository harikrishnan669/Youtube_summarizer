from fastapi import FastAPI, Request
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import re
import asyncio
import threading

# --- FASTAPI APP ---
app = FastAPI()

# Load summarizer
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Extract YouTube video ID
def extract_video_id(url: str):
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    return None

def summarize_youtube(url: str):
    video_id = extract_video_id(url)
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    text = " ".join([t["text"] for t in transcript])

    # Limit text for summarizer
    if len(text) > 2000:
        text = text[:2000]

    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    return summary[0]["summary_text"]

# --- TELEGRAM BOT ---
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send me a YouTube link and I'll summarize it!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    # Simple YouTube link check
    if "youtube.com" in text or "youtu.be" in text:
        await update.message.reply_text("Fetching transcript and summarizing... ⏳")

        try:
            summary = summarize_youtube(text)
            await update.message.reply_text("✨ Summary:\n\n" + summary)
        except Exception as e:
            await update.message.reply_text(f"❌ Error: {str(e)}")
    else:
        await update.message.reply_text("Please send me a valid YouTube link.")

def run_bot():
    import asyncio
    asyncio.set_event_loop(asyncio.new_event_loop())  # create a loop for this thread

    app_bot = Application.builder().token(TOKEN).build()
    app_bot.add_handler(CommandHandler("start", start))
    app_bot.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app_bot.run_polling()


# --- FASTAPI ENDPOINT (Optional: For testing via API) ---
@app.get("/summarize")
def summarize_api(url: str):
    return {"summary": summarize_youtube(url)}

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, FastAPI is live!"}
