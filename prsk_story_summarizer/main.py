from gpt4all import GPT4All
from db import init_db
from scraper import scrape_stories
from manager import get_or_scrape_stories, get_or_scrape_chapters, get_or_scrape_texts
from summarizer import summarize_chapter
from menu import display_main_menu, display_story_menu, display_chapter_menu, display_summary_menu

def main():
    init_db()
    model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")

    selected_action = display_main_menu()
    while selected_action != 0:
        if selected_action == 1:
            scrape_stories()

        # retrieve stories from database
        stories = get_or_scrape_stories()
        selected_story = display_story_menu(stories)

        # retrieve chapters from database
        chapters = get_or_scrape_chapters(selected_story)
        selected_chapters = display_chapter_menu(chapters)

        if (selected_action == 2):
            for selected_chapter in selected_chapters:
                # provide entire chapter text
                text = get_or_scrape_texts(selected_story, selected_chapter)
                print(f"\n\tStory: {selected_story["title"]}")
                print(f"\tChapter: {selected_chapter["title"]}")
                print(text[0]["text"])
        else:
            # provide summary of chapter text
            overwrite_desired = display_summary_menu()
            if overwrite_desired:
                for selected_chapter in selected_chapters:
                    summary = summarize_chapter(model, selected_story, selected_chapter, True)
                    print(f"\n\tStory: {selected_story["title"]}")
                    print(f"\tChapter: {selected_chapter["title"]}")
                    print(summary)
            else:
                for selected_chapter in selected_chapters:
                    summary = summarize_chapter(model, selected_story, selected_chapter, False)
                    print(f"\n\tStory: {selected_story["title"]}")
                    print(f"\tChapter: {selected_chapter["title"]}")
                    print(summary)

        selected_action = display_main_menu()

if __name__ == "__main__":
    main()
