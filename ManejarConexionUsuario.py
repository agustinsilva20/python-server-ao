import Jugador

def handle_client(client_socket, client_address, game_controller):
    # Recibe y maneja comandos del jugador
    # Instancia una clase de Jugador
    player = Jugador(client_socket, client_address, game_controller)

    # Lo agrega a Game Controler
    game_controller.agregar_jugador(player)

    # Lo pone en loop a escuchar comandos
    player.recibir_comandos()