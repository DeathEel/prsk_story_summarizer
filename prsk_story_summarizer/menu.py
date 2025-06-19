import os

def display_main_menu():
    selected_action = loop_menu("Select an action to take: ", ["Refresh stories", "Read stories", "Summarize stories"])
    return selected_action

def display_story_menu(stories):
    selected_story = loop_menu("Select a story: ", [story["title"] for story in stories])
    if selected_story == "q":
        return selected_story
    return stories[selected_story]

def display_chapter_menu(chapters):
    selected_chapter = loop_menu("Select a chapter: ", [chapter["title"] for chapter in chapters] + ["All Chapters"])
    if selected_chapter == "q":
        return selected_chapter
    elif selected_chapter == len(chapters):
        return chapters
    return [chapters[selected_chapter]]

def display_overwrite_menu():
    selected_action = loop_menu("Overwrite summary in database?: ", ["No", "Yes"])
    return selected_action

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def get_valid_input(prompt, lower_bound, upper_bound):
    user_input = input(prompt)
    if user_input == "n" or user_input == "p" or user_input == "q":
        return user_input, ""
    try:
        user_input = int(user_input)
        if lower_bound <= user_input <= upper_bound:
            return user_input, ""
        else:
            return user_input, f"Please enter an integer between {lower_bound} and {upper_bound}, inclusive."
    except ValueError:
        return user_input, "Invalid input. Please enter a valid character or integer."

def display_menu(options, start, page_size, error_message):
    end = min(start + page_size, len(options))
    true_page_size = end - start    # amount of options displayed in page

    # print blanks to prevent menu from moving
    if true_page_size < page_size:
        print("\n" * (page_size - true_page_size - 1))

    # print menu options
    for i in range(start, end):
        print(f"{i + 1}. {options[i]}")
    print("-" * 50)
    print(f"Showing {start + 1}-{end} of {len(options)}")
    print("n: next page | p: previous page | q: quit")
    print(error_message if error_message else "")

    return start, end

def loop_menu(prompt, options):
    start = 0
    page_size = 20
    error = None
    
    while True:
        clear_screen()
        start, end = display_menu(options, start, page_size, error)
        user_input, error = get_valid_input(prompt, start, end)

        if error:
            continue
        elif user_input == "n" and start + page_size >= len(options):
            error = "No next page available."
        elif user_input == "p" and start - page_size < 0:
            error = "No previous page available."
        elif user_input == "q":
            return user_input
        elif user_input == "n":
            start += page_size
        elif user_input == "p":
            start -= page_size
        else:
            return user_input - 1

# testing
if __name__ == "__main__":
    stories = [{"id": 0, "title": "title0", "url": "url0"}, {"id": 1, "title": "title1", "url": "url1"}]
    display_story_menu(stories)
