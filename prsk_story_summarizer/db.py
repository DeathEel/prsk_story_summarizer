import sqlite3
from scraper import scrape_stories, scrape_chapters, scrape_texts

def init_db():
    conn = sqlite3.connect("prsk_stories.db")
    cur = conn.cursor()

	table = ["""
        CREATE TABLE IF NOT EXISTS stories (
	        id INTEGER PRIMARY KEY AUTOINCREMENT,
	        title TEXT NOT NULL,
	        url TEXT NOT NULL
	    );""",
        """
        CREATE TABLE IF NOT EXISTS chapters (
	        story_id INTEGER NOT NULL,
            id INTEGER NOT NULL,
	        title TEXT NOT NULL,
	        url TEXT NOT NULL,
	        PRIMARY KEY (story_id, id),
	        FOREIGN KEY (story_id) REFERENCES stories(id)
	    );""",
        """
        CREATE TABLE IF NOT EXISTS texts (
            story_id INTEGER NOT NULL,
            chapter_id INTEGER NOT NULL,
            text TEXT NOT NULL,
            PRIMARY KEY (story_id, chapter_id),
            FOREIGN KEY (story_id) REFERENCES stories(id),
            FOREIGN KEY (chapter_id) REFERENCES chapters(id)
        );"""
	]
	
	for t in table:
	    cur.execute(t)
	
	conn.commit()
	conn.close()

def add_stories_to_db(stories):
    conn = sqlite3.connect("prsk_stories.db")
    cur = conn.cursor()

    cur.executemany("""
        INSERT OR IGNORE INTO stories VALUES (:id, :title, :url)
    """, stories)

    conn.commit()
    conn.close()

def add_chapters_to_db(chapters):
    conn = sqlite3.connect("prsk_stories.db")
    cur = conn.cursor()

    cur.executemany("""
        INSERT OR IGNORE INTO chapters VALUES (:story_id, :id, :title, :url)
    """, chapters)

    conn.commit()
    conn.close()

def add_text_to_db(text):
    conn = sqlite3.connect("prsk_stories.db")
    cur = conn.cursor()

    cur.execute("""
        INSERT OR IGNORE INTO texts VALUES (:story_id, :chapter_id, :text)
    """, text)

    conn.commit()
    conn.close()

def get_stories():
    conn = sqlite3.connect("prsk_stories.db")
    conn.row_factory = sqlite3.Row  # make rows behave like dicts
    cur = conn.cursor()

    # if stories table not exists, scrape stories
    cur.execute("""
        SELECT name FROM sqlite_master WHERE type='table' AND name='stories';
    """)

    if cur.fetchone() is None:
        scrape_stories()

    # retrieve stories from database
    cur.execute("""
        SELECT * FROM stories
    """)
    stories = cur.fetchall()
    conn.close()

    return stories

def get_chapters(story):
    story_id = story["id"]
    story_link = story["url"]

    conn = sqlite3.connect("prsk_stories.db")
    conn.row_factory = sqlite3.Row  # make rows behave like dicts
    cur = conn.cursor()

    # if chapter not exists, scrape chapters
    cur.execute("""
        SELECT * FROM chapters WHERE story_id = ?
    """, (story_id,))

    if cur.fetchone() is None:
        scrape_chapters(story_id, story_link)

    # retrieve chapters from database
    cur.execute("""
        SELECT * FROM chapters
    """)
    chapters = cur.fetchall()
    conn.close()

    return chapters

def get_texts(story, chapter):
    story_id = story["id"]
    chapter_id = chapter["id"]
    chapter_link = chapter["url"]

    conn = sqlite3.connect("prsk_stories.db")
    conn.row_factory = sqlite3.Row  # make rows behave like dicts
    cur = conn.cursor()

    # if text not exists, scrape text
    cur.execute("""
        SELECT * FROM texts WHERE story_id = ? AND chapter_id = ?
    """, (story_id, chapter_id,))

    if cur.fetchone() is None:
        scrape_texts(story_id, chapter_id, chapter_link)

    # retrieve texts from database
    cur.execute("""
        SELECT * FROM texts
    """)
    texts = cur.fetchall()
    conn.close()

    return texts
