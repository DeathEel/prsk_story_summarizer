import sqlite3

def init_db():
    con = sqlite3.connect("prsk_stories.db")
    cur = con.cursor()

	table = [
	    """ CREATE TABLE IF NOT EXISTS stories (
	            id INTEGER PRIMARY KEY AUTOINCREMENT,
	            title TEXT NOT NULL,
	            url TEXT NOT NULL
	        );""",
	
	    """ CREATE TABLE IF NOT EXISTS chapters (
	            story_id INTEGER NOT NULL,
                id INTEGER NOT NULL,
	            title TEXT NOT NULL,
	            url TEXT NOT NULL,
	            PRIMARY KEY (story_id, id),
	            FOREIGN KEY (story_id) REFERENCES stories(id)
	        );""",

        """ CREATE TABLE IF NOT EXISTS texts (
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
	
	con.commit()
	con.close()

def add_story_to_db(story):
    con = sqlite3.connect("prsk_stories.db")
    cur = con.cursor()

    cur.execute("""
            INSERT INTO stories VALUES (:id, :title, :url)
    """, story)

    con.commit()
    con.close()

def add_chapter_to_db(chapter):
    con = sqlite3.connect("prsk_stories.db")
    cur = con.cursor()

    cur.execute("""
            INSERT INTO chapters VALUES (:story_id, :id, :title, :url)
    """, story)

    con.commit()
    con.close()

def add_text_to_db(text):
    # text is a dict with story_id, chapter_id, text
    con = sqlite3.connect("prsk_stories.db")
    cur = con.cursor()

    cur.execute("""
            INSERT INTO texts VALUES (:story_id, :chapter_id, :text)
    """, story)

    con.commit()
    con.close()
