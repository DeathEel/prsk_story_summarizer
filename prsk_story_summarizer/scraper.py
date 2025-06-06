from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from db import add_story_to_db, add_chapter_to_db, add_text_to_db

def scrape_stories():
    html = render_page("https://sekai.best/storyreader/eventStory")
    soup = BeautifulSoup(html, "html.parser")

    # scrape story titles
    story_title_tags = soup.find_all(class_="MuiTypography-root MuiTypography-body1 css-3kq318")
    story_titles = []
    for idx, story_title_tag in enumerate(story_title_tags):
        if idx == 0:
            continue
        story_titles.append(story_title_tag.text.strip())

    # scrape story links
    story_link_tags = soup.find_all(class_="MuiBox-root css-f02xnr")
    story_links = []
    for story_link_tag in story_link_tags:
        story_link = "https://sekai.best" + story_link_tag["href"]
        story_links.append(story_link)

    # combine all data and add to database
    stories = []
    for idx, story in enumerate(reversed(list(zip(story_titles, story_links)))):
        story_dict = dict(id=idx,title=story[0], url=story[1])
        stories.append(story_dict)

    add_story_to_db(stories)

def scrape_chapters(story_id, story_link):
    html = render_page(story_link)
    soup = BeautifulSoup(html, "html.parser")

    # scrape chapter titles
    chapter_title_tags = soup.find_all(class_="MuiTypography-root MuiTypography-body1 css-3kq318")
    chapter_titles = []
    for idx, chapter_title_tag in enumerate(chapter_title_tags):
        if idx == 0:
            continue
        chapter_titles.append(chapter_title_tag.text.strip())

    # scrape chapter links
    chapter_link_tags = soup.find_all(class_="MuiBox-root css-f02xnr")
    chapter_links = []
    for chapter_link_tag in chapter_link_tags:
        chapter_link = "https://sekai.best" + chapter_link_tag["href"]
        chapter_links.append(chapter_link)

    # combine all data and add to database
    chapters = []
    for idx, chapter in enumerate(list(zip(chapter_titles, chapter_links))):
        chapter_dict = dict(story_id=story_id, id=idx, title=chapter[0], url=chapter[1])
        chapters.append(chapter_dict)
    
    add_chapter_to_db(chapters)

def scrape_texts(story_id, chapter_id, chapter_link):
    html = render_page(chapter_link)
    soup = BeautifulSoup(html, "html.parser")

    # scrape speaker
    speaker_tags = soup.find_all(class_="MuiChip-label MuiChip-labelMedium css-9iedg7")
    speakers = []
    for idx, speaker_tag in enumerate(speaker_tags):
        speaker = speaker_tag.text.strip()
        if speaker in ["Release Condition", "Background Change", "Background Music", "Sound Effect"]:
            continue
        speakers.append(speaker)

    # scrape line
    line_tags = soup.find_all(class_="MuiTypography-root MuiTypography-body1 css-5kc7yo")
    lines = []
    for line_tag in line_tags:
        line = line_tag.text.strip().replace("\n", " ")
        if line in ["No Sound"]:
            continue
        lines.append(line)

    # combine speakers and lines
    text = ""
    for speaker_and_line in list(zip(speakers, lines)):
        text = text + speaker_and_line[0] + ": "
        text = text + speaker_and_line[1] + "\n"

    # combine all data and add to database
    text_dict = dict(story_id=story_id, chapter_id=chapter_id, text=text)
    add_text_to_db(text_dict)

def render_page(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)

        region = None
        while region != "en":
            page.evaluate("""
	             const settings = JSON.parse(localStorage.getItem('settings') || '{}');
	             settings.region = 'en';
	             localStorage.setItem('settings', JSON.stringify(settings));
	        """)
            page.goto(url)
            region = page.evaluate("JSON.parse(localStorage.getItem('settings')).region")

        page.wait_for_load_state("networkidle")
        html = page.content()
        browser.close()
        return html

# testing
if __name__ == "__main__":
    #html = render_page("https://sekai.best/storyreader/eventStory/64/4")
    #with open("output.html", "w", encoding="utf-8") as file:
    #    file.write(BeautifulSoup(html, "html.parser").prettify())
    #scrape_stories()
    #scrape_chapters(62, "https://sekai.best/storyreader/eventStory/64") 
    #text = scrape_text(62, 4, "https://sekai.best/storyreader/eventStory/64/4")
    #print(text["text"])
