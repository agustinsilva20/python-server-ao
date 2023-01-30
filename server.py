import socket
import threading
import time
import sys

from ControladorJuego import ControladorJuego
import ManejarConexionUsuario


class Server():
    def __init__(self):
        self.server_on = True

    def set_server_offline(self):
        self.server_on = False
    
    def start(self):
        game_controller = ControladorJuego()
        game_controller.load_world()

        # Creo un hilo encargado de procesar los comandos de los clientes 
        comandos_thread = threading.Thread(target=game_controller.procesar_comandos)
        comandos_thread.start()

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("127.0.0.1", 7666))

        # Escuchamos hasta 5 conexiones
        server_socket.listen(5)

        # Informar en consola
        print("Servidor iniciado correctamente! \n Escuchando nuevas conexiones...")


        # Aceptar nuevas conexiones: Hilo principal
        while self.server_on:
            client_socket, client_address = server_socket.accept()
            print("Nueva conexion desde", client_address)

            # Para cada nueva conexion, inicio un nuevo Hilo: Este hilo sera el encargado de Recibir y enviar paquetes al cliente
            client_thread = threading.Thread(target=ManejarConexionUsuario.handle_client, args=(client_socket, client_address, game_controller))
            client_thread.start()
        
        print("Dejando de escuchar conexiones. Vuelva a encender el servidor")
    

def server():
    # Creo una instancia del servidor
    server = Server()

    # En un hilo me corro el servidor
    server_thread = threading.Thread(target = server.start)
    server_thread.start()

    # En otro hilo me quedo a la espera del comando de salida del servidor
    time.sleep(2)
    while server.server_on:
        entrada = input("Ingrese 'exit' para cerrar servidor: ")
        if entrada.upper() == "EXIT":
            server.set_server_offline()
        else:
            print("Comando no reconocido")
    
    print("Servidor finalizado correctamente")
server()


