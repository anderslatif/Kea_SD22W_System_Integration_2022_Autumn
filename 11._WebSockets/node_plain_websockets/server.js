import WebSocket, { WebSocketServer } from "ws";

const websocketServer = new WebSocketServer({ port: 8080 });

websocketServer.on("connection", (ws) => {
    ws.on("message", (message) => {
        console.log(`Received message => ${message}`);
    });
    ws.send("Hello! Message From Server!!!");
});
