def display_story_menu(stories):
    for idx, story in enumerate(stories):
        print(f"{idx}: {story['title']}")
    selected_index = get_int_input(f"Select the story to read the summary of: ", 0, len(stories) - 1)
    return stories[selected_index]

def display_chapter_menu(chapters):
    for idx, chapter in enumerate(chapters):
        print(f"{idx}: {chapter['title']}")
    selected_index = get_int_input(f"Select the chapter to read the summary of: ", 0, len(chapters) - 1)
    return chapters[selected_index]

def get_int_input(prompt, lower_bound, upper_bound):
    while True:
        try:
            user_input = int(input(prompt))
            if lower_bound <= user_input <= upper_bound:
                return user_input
            else:
                print(f"Please enter an integer between {lower_bound} and {upper_bound}, inclusive.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# testing
if __name__ == "__main__":
    stories = [{"id": 0, "title": "ligma", "url": "ligmaagain"}, {"id": 1, "title": "not ligma", "url": "notligmaagain"}]
    display_story_menu(stories)
