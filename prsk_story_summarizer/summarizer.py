from manager import get_or_scrape_texts
from db import add_summary_to_db

def summarize_chapter(model, story, chapter, overwrite):
    text = get_or_scrape_texts(story, chapter)
    if text[0]["summary"] and not overwrite:
        return text[0]["summary"]

    prompt = f"You are a summarizer for a fictional story. You will be provided with the text of a chapter from this story. This text will be a blend of dialogue, captions, and internal monologue (indicated by parentheses). Voice calls are represented using angle brackets. Your task is to generate a summary of the provided chapter for players to read when they want to remember key events and interactions. Your response must strictly contain only the summary; do not write extra text before or after the summary.\n\n\n{text[0]['text']}\n\n\nSummary:"

    with model.chat_session():
        summary = model.generate(prompt)
        add_summary_to_db(summary, story["id"], chapter["id"])

        return summary
