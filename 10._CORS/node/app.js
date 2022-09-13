import express from "express";
const app = express();

import cors from "cors";
app.use(cors());

app.get("/message", (req, res) => {
    res.send({ message: "Hello from Express" });
});


app.listen(8080, () => console.log("Server is running on port", 8080));
