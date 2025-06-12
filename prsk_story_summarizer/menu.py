def display_main_menu():
    print("\n0. Quit\n1. Refresh stories\n2. Read stories\n3. Summarize stories")
    selected_action = get_int_input(f"Select an action to take: ", 0, 3)
    return selected_action

def display_story_menu(stories):
    print("")
    for idx, story in enumerate(stories):
        print(f"{idx}: {story['title']}")
    selected_index = get_int_input(f"Select a story: ", 0, len(stories) - 1)
    return stories[selected_index]

def display_chapter_menu(chapters):
    print("")
    for idx, chapter in enumerate(chapters):
        print(f"{idx}: {chapter['title']}")
    print(f"{len(chapters)}: All Chapters")
    selected_index = get_int_input(f"Select a chapter: ", 0, len(chapters))

    if selected_index == len(chapters):
        return chapters

    return [chapters[selected_index]]

def display_summary_menu():
    print("\n0. No\n1. Yes")
    selected_action = get_int_input(f"Overwite summary in database?: ", 0, 1)
    return selected_action

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
    stories = [{"id": 0, "title": "title0", "url": "url0"}, {"id": 1, "title": "title1", "url": "url1"}]
    display_story_menu(stories)
