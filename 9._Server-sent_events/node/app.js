import express from "express";
const app = express();

app.use(express.static("public"));

app.get("/synchronizeTime", (req, res) => {
    res.writeHead(200, {
        "Content-Type": "text/event-stream",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive"
    });
    setInterval(() => {
        res.write("data: " + new Date() + "\n\n");
    }, 1000);
});

app.listen(8080, () => console.log("Server is running on port", 8080));
