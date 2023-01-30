import queue

class ControladorJuego:
    def __init__(self):
        self.jugadores = []
        self.cola_comandos = queue.Queue()

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

    def agregar_comando(self, jugador, comando):
        self.cola_comandos.put((jugador, comando))

    def procesar_comandos(self):
        while True:
            jugador, comando = self.cola_comandos.get()
            # procesar comando y actualizar estado del juego
