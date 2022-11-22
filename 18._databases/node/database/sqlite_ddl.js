import db from "./connection.js";

db.exec(`
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY,
        project_type TEXT,
        project_name TEXT
    )
`);