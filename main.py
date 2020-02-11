import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('connection established')

@sio.on('new message')
def on_message(data):
    print('I received a message!', data)
    def replace_all(repls, str):
        # return re.sub('|'.join(repls.keys()), lambda k: repls[k.group(0)], str)
            return re.sub('|'.join(re.escape(key) for key in repls.keys()),
            lambda k: repls[k.group(0)], str) 
    nombreAsistente = "JEFFERSON"
    apellidoAsistente = "AGUILAR"
    empresa = "ALUN IDEAS"
    tipoVisitante = "VISITANTE"
    asistenteId = "ASJDUFNESKFSDLFKJSDLKFJSDL - UUID"
    impresoraAsignada = "GT800-1"
    label = """
    ^XA
    ^FO100, 30
    ^A0,65,40^FH
    ^FD"""+nombreAsistente+"""^FS
    ^FO100, 90
    ^A0,65,40^FH
    ^FD"""+apellidoAsistente+"""^FS
    ^FO100, 160
    ^A0,40,25^FH
    ^FD"""+empresa+"""^FS
    ^FO100, 240
    ^A0,40,25^FH
    ^FD"""+tipoVisitante+"""^FS
    ^FO600,220
    ^BQN,2,5
    ^FDMA,"""+tipoVisitante+"-"+str(asistenteId)+"""^FS
    ^XZ
    """
    from zebra import zebra
    z = zebra(impresoraAsignada)
    z.output(label)

@sio.event
def message(data):
    print('message received with ', data)
    sio.emit('my response', {'response': 'my response'})

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://localhost:3000')
sio.wait()