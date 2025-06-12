from manager import get_or_scrape_texts
from db import add_summary_to_db

def summarize_chapter(model, tokenizer, story, chapter, overwrite):
    text = get_or_scrape_texts(story, chapter)
    if text[0]["summary"] and not overwrite:
        return text[0]["summary"]

    prompt = f"Summarize the following fictional story in a single paragraph of around five sentences (approximately 50 words). The summary should provide an objective recounting of key events, focusing on the characters' interactions and especially noting when characters meet for the first time. Avoid interpretation or speculation. Assume the reader has already read the story and needs a factual, concise refresher. Do not repeat this prompt or explain your response.\n\nStory:\n{text[0]['text']}\n\nSummary:\n"

    summary = model(prompt, max_new_tokens=300, do_sample=False, return_full_text=False, eos_token_id=tokenizer.eos_token_id, stop_sequence=["\n\n"])[0]["generated_text"].strip().split("\n\n")[0].strip()
    add_summary_to_db(summary, story["id"], chapter["id"])

    return summary
