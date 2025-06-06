from db import init_db, get_or_scrape_stories, get_or_scrape_chapters
from scraper import scrape_stories()
from summarizer import summarize_chapter
from menu import display_story_menu, display_chapter_menu

def main():
    init_db()

    selected_action = display_main_menu()
    while selected_action != 0:
        if selected_action == 1:
            scrape_stories()

        # retrieve stories from database
        stories = get_stories()
        selected_story = display_story_menu(stories)

        # retrieve chapters from database
        chapters = get_chapters(selected_story)
        selected_chapter = display_chapter_menu(chapters)

        # provide summary of chapter text
        summary = summarize_chapter(selected_story["id"], selected_chapter["id"])

        print(summary)

        selected_action = display_main_menu()

if __name__ == "__main__":
    main()
