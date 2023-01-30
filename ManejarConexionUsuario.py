from Jugador import Jugador

def handle_client(client_socket, client_address, game_controller):
    # Recibe y maneja comandos del jugador
    player = Jugador(client_socket, client_address, game_controller) # Instancia una clase de Jugador
    print("Instancia de jugador creada en un nuevo hilo")

    # Lo agrega a Game Controler
    game_controller.agregar_jugador(player)

    # Lo pone en loop a escuchar comandos
    player.recibir_comandos()