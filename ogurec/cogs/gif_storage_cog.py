import sqlite3
import time
import random

class GifStorage:
    def __init__(self, path="gifs.db"):
        self.conn = sqlite3.connect(path)
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS gifs(
            id INTEGER PRIMARY KEY,
            url TEXT UNIQUE,
            added_at INTEGER
        )
        """)
        self.conn.commit()

    def add(self, url: str):
        self.conn.execute(
            "INSERT OR IGNORE INTO gifs(url, added_at) VALUES(?, ?)",
            (url, int(time.time()))
        )
        self.conn.commit()

    def cleanup(self):
        week = 7 * 24 * 3600
        self.conn.execute(
            "DELETE FROM gifs WHERE added_at < ?",
            (int(time.time()) - week,)
        )
        self.conn.commit()

    def random(self):
        self.cleanup()

        cur = self.conn.execute(
            "SELECT url FROM gifs ORDER BY RANDOM() LIMIT 1"
        )
        row = cur.fetchone()

        return row[0] if row else None
    