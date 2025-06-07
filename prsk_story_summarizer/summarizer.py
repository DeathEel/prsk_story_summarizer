from manager import get_or_scrape_texts

def summarize_chapter(model, story, chapter):
    text = get_or_scrape_texts(story, chapter)
    if text[0]["summary"]:
        return text[0]["summary"]

    prompt = f"You are a summarizer for a fictional story. You will be provided with the text of a chapter from this story. This text will be a blend of dialogue, captions, and internal monologue (indicated by parentheses). Voice calls are represented using angle brackets. Your task is to generate a summary of the provided chapter for players to read when they want to remember key events and interactions. Your response must strictly contain only the summary; do not write extra text before or after the summary.\n\n\n{text[0]['text']}\n\n\nSummary:"

    print(prompt)

    with model.chat_session():
        return model.generate(prompt)
