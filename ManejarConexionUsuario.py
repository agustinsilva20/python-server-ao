from Cliente import Cliente

def handle_client(client_socket, client_address, game_controller):
    # Recibe y maneja comandos del Clientes
    player = Cliente(client_socket, client_address, game_controller) # Instancia una clase de Cliente
    print("Instancia de Cliente creada en un nuevo hilo")

    # Lo agrega a Game Controler
    game_controller.agregar_cliente(player)

    # Lo pone en loop a escuchar comandos
    player.recibir_comandos()