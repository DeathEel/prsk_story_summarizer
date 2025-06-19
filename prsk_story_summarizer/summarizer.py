from manager import get_or_scrape_texts
from db import add_summary_to_db

def summarize_chapter(model, tokenizer, story, chapter, overwrite):
    texts = get_or_scrape_texts(story, chapter)
    if texts["summary"] and not overwrite:
        return texts["summary"]

    prompt = f"Summarize the following fictional story in a single paragraph of around five sentences (approximately 50 words). The story is in the form of a transcript: a blend of dialogue, captions, and internal monologue (indicated by parentheses). Voice calls are represented using angle brackets. The summary should provide an objective recounting of key events, focusing on the characters' interactions and especially noting when characters meet for the first time. Avoid interpretation or speculation. Assume the reader has already read the story and needs a factual, concise refresher. Do not repeat this prompt or explain your response.\n\nStory:\n{texts['transcript']}\n\nSummary:\n"

    summary = model(prompt, max_new_tokens=300, do_sample=False, return_full_text=False, eos_token_id=tokenizer.eos_token_id, stop_sequence=["\n\n"])[0]["generated_text"].strip().split("\n\n")[0].strip()
    add_summary_to_db(summary, story["id"], chapter["id"])

    return summary
