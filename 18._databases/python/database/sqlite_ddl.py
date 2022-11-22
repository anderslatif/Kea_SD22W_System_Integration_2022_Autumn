import sqlite3

con = sqlite3.connect('montypython.db')

con.execute('''
    CREATE TABLE projects (
        id INTEGER PRIMARY KEY,
        project_type TEXT,
        project_name TEXT
    )
''')

con.close()
