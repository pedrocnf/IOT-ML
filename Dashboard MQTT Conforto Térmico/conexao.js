function conectar_mqtt(){
    var ssl = document.querySelector('input[name = seguranca]:checked').value;
    var servidor = document.getElementById("servidor").value;
    var porta = document.getElementById("porta").value;
    var cliente = document.getElementById("cliente").value;
    var usuario = document.getElementById("usuario").value;
    var senha = document.getElementById("senha").value;
    client = new Paho.MQTT.Client(servidor, Number(porta),cliente);
    client.onConnectionLost = onConnectionLost;
    client.onMessageArrived = onMessageArrived;
    var options = {
      useSSL: Boolean(ssl),
      userName: usuario,
      password: senha,
      onSuccess:onConnect,
      onFailure:doFail
    }
    client.connect(options)
  }
  
  function onConnect() {
    client.subscribe("/cloudmqtt");
    message = new Paho.MQTT.Message("Hello CloudMQTT");
    message.destinationName = "/cloudmqtt";
    client.send(message);
      alert("Conectado em SErvidor MQTT")
    gravar('Servidor MQTT', 'Conectado')
  }
  
  function doFail(e){
    console.log(e);
  }
  
  function onConnectionLost(responseObject) {
    if (responseObject.errorCode !== 0) {
      console.log("onConnectionLost:"+responseObject.errorMessage);
    }
  }
  
  function onMessageArrived(message) {
    console.log("onMessageArrived:"+message.payloadString);
  }