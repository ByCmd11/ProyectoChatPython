import socket
import threading

# Direcion ip y puerto
host = '127.0.0.1'
port = 55555
# Creamos el socket tcp que usara internet
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Asignamos el host y el puerto
server.bind((host, port))
server.listen()
print(f"El servidor esta funcionando en {host}:{port}")

# arrays que contendran los clientes y los nombres de usuarios
clientes = []
usuarios = []
# Funcipn que enviara los mensajes a los demas clientes


def transmision(mensaje, _cliente):
    for cliente in clientes:
        if cliente != _cliente:
            cliente.send(mensaje)

# Funcion que recibira los mendajes escritos por los clientes


def mensajes(cliente):
    while True:
        try:
            mensaje = cliente.recv(1024)
            transmision(mensaje, cliente)
            historial(mensaje.decode('utf-8'))
        except:
            indice = cliente.index(cliente)
            usuario = usuarios[indice]
            transmision(
                f"Sistema: {usuario} desconectado".encode('utf-8'), cliente)
            clientes.remove(cliente)
            usuarios.remove(usuario)
            cliente.close()
            break


def conexiones():
    while True:
        cliente, direccion = server.accept()

        cliente.send("@usuario".encode("utf-8"))
        usuario = cliente.recv(1024).decode('utf-8')

        clientes.append(cliente)
        usuarios.append(usuario)

        print(f"{usuario} esta conectado {str(direccion)}")

        mensaje = f"Sistema: {usuario} se ha unido al chat".encode("utf-8")
        transmision(mensaje, cliente)
        cliente.send("Se ha conectado ".encode("utf-8"))

        thread = threading.Thread(target=mensajes, args=(cliente,))
        thread.start()



def historial(mensaje):

    file = open('PYTHONFCT.txt', 'a')
    file.write(mensaje+"\n")
    file.close()


conexiones()
