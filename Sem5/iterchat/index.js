const webSocket = new WebSocket('ws://localhost:8888/websocket');

webSocket.onopen = () => {
    webSocket.send("opened");
};

webSocket.onmessage = () => {
    webSocket.send("Send message");
};

webSocket.onclose = () => {
    webSocket.send("closed");
};