import socket
import threading


usuario = input("Introduce tu usuario: ")
host = "127.0.0.1"
puerto = 55555

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect((host, puerto))


def recivirMensaje():
    while True:
        try:
            mensaje = cliente.recv(1024).decode("utf-8")

            if mensaje == "@usuario":
                cliente.send(usuario.encode("utf-8"))
            else:
                print(mensaje)

        except:
            print("Se ha perdido la conexion")
            cliente.close()
            break


def escribirMensaje():
    while True:

        mensaje = f"{usuario}: {input('')}"
        cliente.send(mensaje.encode("utf-8"))


recivir_hilo = threading.Thread(target=recivirMensaje)
recivir_hilo.start()

escribir_hilo = threading.Thread(target=escribirMensaje)
escribir_hilo.start()
