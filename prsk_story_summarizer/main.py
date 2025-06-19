from db import init_db
from scraper import scrape_stories
from manager import get_or_scrape_stories, get_or_scrape_chapters, get_or_scrape_texts
from summarizer import summarize_chapter
from menu import display_main_menu, display_story_menu, display_chapter_menu, display_overwrite_menu
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline, logging

def main():
    init_db()

    logging.set_verbosity_error()

    model_name = "ibm-granite/granite-3.3-8b-instruct"
    cache_dir = "llm/"

    tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=cache_dir, use_fast=False)
    model = AutoModelForCausalLM.from_pretrained(model_name, cache_dir=cache_dir, torch_dtype="auto", device_map="auto")

    menu_stack = [("main", lambda: display_main_menu())]

    while menu_stack:
        current_menu_type, current_menu_function = menu_stack[-1]
        selected_action = current_menu_function()

        # main menu
        if current_menu_type == "main":
            if selected_action == "q":
                menu_stack.pop()
            elif selected_action != 0:
                summarize = True if selected_action == 2 else False
                stories = get_or_scrape_stories()
                menu_stack.append(("story", lambda: display_story_menu(stories)))
            else:
                scrape_stories()

        # story menu
        elif current_menu_type == "story":
            if selected_action == "q":
                menu_stack.pop()
            else:
                selected_story = selected_action
                chapters = get_or_scrape_chapters(selected_story)
                menu_stack.append(("chapter", lambda: display_chapter_menu(chapters)))

        # chapter menu
        elif current_menu_type == "chapter":
            if selected_action == "q":
                menu_stack.pop()
                continue

            selected_chapters = selected_action

            if summarize:
                menu_stack.append(("overwrite", lambda: display_overwrite_menu()))
            else:
                for selected_chapter in selected_chapters:
                    transcript = get_or_scrape_texts(selected_story, selected_chapter)["transcript"]
                    print(f"\n\tStory: {selected_story["title"]}")
                    print(f"\tChapter: {selected_chapter["title"]}")
                    print(transcript)
                    input("\nPress Enter to continue.")

                menu_stack = [("main", lambda: display_main_menu())]

        # overwrite menu
        elif current_menu_type == "overwrite":
            if selected_action == "q":
                menu_stack.pop()
            else:
                overwrite = selected_action
                for selected_chapter in selected_chapters:
                    summarizer_model = pipeline("text-generation", model=model, tokenizer=tokenizer)
                    summary = summarize_chapter(summarizer_model, tokenizer, selected_story, selected_chapter, overwrite)
                    print(f"\n\tStory: {selected_story["title"]}")
                    print(f"\tChapter: {selected_chapter["title"]}")
                    print(summary)
                    input("\nPress Enter to continue.")

                menu_stack = [("main", lambda: display_main_menu())]

if __name__ == "__main__":
    main()
