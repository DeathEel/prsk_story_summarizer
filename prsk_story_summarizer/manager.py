from db import get_stories, get_chapters, get_texts, add_stories_to_db, add_chapters_to_db, add_transcript_to_db
from scraper import scrape_stories, scrape_chapters, scrape_transcript

def get_or_scrape_stories():
    stories = get_stories()
    if not stories:
        scraped_stories = scrape_stories()
        add_stories_to_db(scraped_stories)
        stories = get_stories()
    return stories

def get_or_scrape_chapters(story):
    chapters = get_chapters(story)
    if not chapters:
        scraped_chapters = scrape_chapters(story["id"], story["url"])
        add_chapters_to_db(scraped_chapters)
        chapters = get_chapters(story)
    return chapters

def get_or_scrape_texts(story, chapter):
    texts = get_texts(story, chapter)

    # if transcript not found, scrape it
    if not texts or not texts[0]["transcript"]:
        scraped_transcript = scrape_transcript(story["id"], chapter["id"], chapter["url"])
        add_transcript_to_db(scraped_transcript)
        texts = get_texts(story, chapter)
    return texts[0]
