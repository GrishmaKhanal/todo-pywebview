import os
import webview
import sqlite3
from ui import get_index_window

class NoteApp:
    def __init__(self, db_path='notes.db'):
        self.db_path = db_path
        self.init_db()

    def init_db(self):
        db_full_path = os.path.join(os.path.dirname(__file__), self.db_path)
        conn = sqlite3.connect(db_full_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    def get_notes(self):
        db_full_path = os.path.join(os.path.dirname(__file__), self.db_path)
        conn = sqlite3.connect(db_full_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, content FROM notes ORDER BY id DESC")
        notes = cursor.fetchall()
        conn.close()
        # Return a list of dictionaries representing each note
        return [{"id": note[0], "content": note[1]} for note in notes]

    def add_note(self, content):
        if not content.strip():
            return {"error": "Empty note content"}
        db_full_path = os.path.join(os.path.dirname(__file__), self.db_path)
        conn = sqlite3.connect(db_full_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO notes (content) VALUES (?)", (content,))
        conn.commit()
        note_id = cursor.lastrowid
        conn.close()
        return {"id": note_id, "content": content}

if __name__ == '__main__':
    note_app = NoteApp()
    get_index_window(note_app=note_app)
    webview.start(gui='qt')
