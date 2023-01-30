import struct

class Jugador:
    def __init__(self, socket, address, game_controller):
        self.socket = socket
        self.address = address
        self.game_controller = game_controller

    def recibir_comandos(self):
        print("Jugador nuevo: Escuchando datos")
        while True:
            # Recibe los primeros 4 bytes del mensaje en el socket
            tamaño_paquete = self.socket.recv(4)
            if not tamaño_paquete:
                break
            tamaño_paquete = struct.unpack("!I", tamaño_paquete)[0] # Desempaqueta los 4 bytes. se usa para determinar cuantos bytes debe recibir la funcion "recv()"

            # recibir el paquete completo
            paquete = b""
            while len(paquete) < tamaño_paquete:
                paquete += self.socket.recv(tamaño_paquete - len(paquete))

            print("Paquete recivido: " + str(paquete))
            self.game_controller.agregar_comando(self, paquete)

    def enviar_datos(self, data):
        tamaño_paquete = struct.pack("!I", len(data))
        self.socket.sendall(tamaño_paquete + data)
