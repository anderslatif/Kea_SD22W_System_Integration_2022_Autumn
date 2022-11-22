import sqlite3

con = sqlite3.connect('montypython.db')

cursor = con.execute('''Select * from projects''')
projects = cursor.fetchall()

for projectId, projectType, projectName in projects:
    print(projectId, projectType, projectName)
    print("*" * 50)