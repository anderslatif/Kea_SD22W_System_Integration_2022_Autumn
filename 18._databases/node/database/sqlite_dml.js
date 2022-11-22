import db from "./connection.js";

await db.exec('INSERT INTO projects (project_type, project_name) VALUES ("web", "Monty Python");');

const projects = await db.all('SELECT * FROM projects;')
console.log(projects);
