from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def get_stories():
    html = render_page("https://sekai.best/storyreader/eventStory")
    soup = BeautifulSoup(html, "html.parser")

    # get story titles
    story_title_tags = soup.find_all(class_="MuiTypography-root MuiTypography-body1 css-3kq318")
    story_titles = []
    for idx, story_title_tag in enumerate(story_title_tags):
        if idx == 0:
            continue
        story_titles.append(story_title_tag.text.strip())

    # get story links
    story_link_tags = soup.find_all(class_="MuiBox-root css-f02xnr")
    story_links = []
    for story_link_tag in story_link_tags:
        story_link = "https://sekai.best" + story_link_tag["href"]
        story_links.append(story_link)

    # combine to database
    stories = []
    for idx, story in enumerate(reversed(list(zip(story_titles, story_links)))):
        story_dict = dict(id=idx,title=story[0], url=story[1])
        stories.append(story_dict)
        add_story_to_db(story_dict)

    return stories

def get_chapters(story_id, story_link):
    html = render_page(story_link)
    soup = BeautifulSoup(html, "html.parser")

    # get chapter titles
    chapter_title_tags = soup.find_all(class_="MuiTypography-root MuiTypography-body1 css-3kq318")
    chapter_titles = []
    for idx, chapter_title_tag in enumerate(chapter_title_tags):
        if idx == 0:
            continue
        chapter_titles.append(chapter_title_tag.text.strip())

    # get chapter links
    chapter_link_tags = soup.find_all(class_="MuiBox-root css-f02xnr")
    chapter_links = []
    for chapter_link_tag in chapter_link_tags:
        chapter_link = "https://sekai.best" + chapter_link_tag["href"]
        chapter_links.append(chapter_link)

    # combine to database
    chapters = []
    for idx, chapter in enumerate(list(zip(chapter_titles, chapter_links))):
        chapter_dict = dict(story_id=story_id, id=idx, title=chapter[0], url=chapter[1])
        chapters.append(chapter_dict)
        add_chapter_to_db(chapter_dict)

    return chapters

# def get_chapter_text(chapter_link):
    # something

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
    #html = render_page("https://sekai.best/storyreader/eventStory/64")
    #with open("output.html", "w", encoding="utf-8") as file:
    #    file.write(BeautifulSoup(html, "html.parser").prettify())
    #get_stories()
    get_chapters(62, "https://sekai.best/storyreader/eventStory/64") 
