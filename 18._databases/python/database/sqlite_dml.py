import sqlite3

con = sqlite3.connect('montypython.db')

def insert_project(project_type, project_name):
    con.execute('''
        INSERT INTO projects (project_type, project_name)
        VALUES (?, ?)
    ''', (project_type, project_name))
    con.commit()

    