import sqlite3

def init_db():
    conn = sqlite3.connect("stories.db")
    cur = conn.cursor()

	table = [
	    """ CREATE TABLE IF NOT EXISTS stories (
	            id INTEGER PRIMARY KEY AUTOINCREMENT,
	            title TEXT NOT NULL,
	            url TEXT NOT NULL
	        );""",
	
	    """ CREATE TABLE IF NOT EXISTS chapters (
	            id INTEGER NOT NULL,
	            story_id INTEGER NOT NULL,
	            title TEXT NOT NULL,
	            url TEXT NOT NULL,
	            text TEXT NOT NULL,
	            PRIMARY KEY (id, story_id),
	            FOREIGN KEY (story_id) REFERENCES stories(id)
	        );"""
	]
	
	for t in table:
	    cur.execute(t)
	
	conn.commit()
	conn.close()
