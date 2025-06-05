from db import init_db
from scraper import get_stories, get_chapters
from summarizer import summarize_chapter
from menu import display_story_menu, display_chapter_menu

def main():
    init_db()

    user_input = 1
    while user_input != 0:
        stories = get_stories()
        selected_story = display_story_menu(stories)

        chapters = get_chapters(selected_story["id"], selected_story["url"])
        selected_chapter = display_chapter_menu(chapters)

        summary = summarize_chapter(selected_story["id"], selected_chapter["id"])

        print(summary)

        user_input = int(input("\nChoose 0 to quit. Choose 1 to continue."))

if __name__ == "__main__":
    main()
