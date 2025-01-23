import sqlite3

con=sqlite3.connect("youtube_manager.db")
cur=con.cursor()
cur.execute('''
            CREATE TABLE IF NOT EXISTS videos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            duration TEXT NOT NULL
            )
''')

def main():
    pass

if __name__=='__main__':
    main()