import express from "express";
import http from "http";
const app = express();
const server = http.createServer(app);

app.use(express.static("public"));

import { Server } from "socket.io";
const io = new Server(server);

io.on("connection", (socket) => {
    socket.on("ping", (data) => {
        socket.emit("pong", data);
    });

});


server.listen(8080, () => console.log("Server is running on port", 8080));
