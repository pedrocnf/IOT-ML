var express = require('express');

var app = express();
var server = app.listen(4000, () => { 
    console.log("Servidor criado em http://localhost:4000");
})

var io = require('socket.io')(server); 

app.use(express.static('public')); 

const SerialPort = require('serialport'); 
const Readline = SerialPort.parsers.Readline;
const port = new SerialPort('COM4'); 
const parser = port.pipe(new Readline({delimiter: '\r\n'})); 
parser.on('data', (dados) => { 
    console.log("Dados recebidos pela serial: ",dados);
    io.sockets.emit('dados', {dados}); 
});

io.on('connection', (socket) => {
    console.log("Página conectada"); 
})