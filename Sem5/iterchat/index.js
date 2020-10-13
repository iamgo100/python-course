const webSocket = new WebSocket('http://localhost:8888/index');

webSocket.onopen = event => {
    alert('onopen');
    webSocket.send("Hello Web Socket!");
};

webSocket.onmessage = event => {
    alert('onmessage, ' + event.data);
};

webSocket.onclose = event => {
    alert('onclose');
};