from manager import get_or_scrape_texts

def summarize_chapter(model, story, chapter):
    text = get_or_scrape_texts(story, chapter)

    prompt = f"You are a summarizer for a fictional story. You will read one chapter of this story. It is given in the form of dialogue and captions. To indicate that a person is thinking, parentheses are used. To indicate that a person is speaking through a voice call, angle brackets are used. Please provide a summary for players to read when they want to remember key events from each chapter. Do not make commentary about the chapter itself. You are only able to summarize what happened in the story. You cannot make any thoughtful notes about it.\n\n\n{text}\n\n\nSummary:"

    with model.chat_session():
        return model.generate(prompt)
