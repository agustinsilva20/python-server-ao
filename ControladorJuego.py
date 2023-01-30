import queue
import json

from Personaje import Personaje

class ControladorJuego:
    def __init__(self):
        self.clientes = [] # Arreglo de instancia de Clientes
        self.server_on = True

        self.configuracion = {} # Lista de configuracion
        self.hechizos = {} # Lista de hechizos: Dentro tiene objetos, acceder mediante [id][atributo] ejemplo: print(self.hechizos[0]["name"])
        self.objetos = {} # Lista de Objetos
        self.npc = {} # Lista de NPCs


        self.cola_comandos = queue.Queue()

    def load_world(self):
        print("Iniciando Mundo Zhendrek AO..")
        print("Cargando Server.json")
        self.configuracion = self.load_json("server.json")
        print("OK!")
        print("Cargando Mapas")
        print("ERROR! No desarrollado aun")
        print("Cargando Hechizos.json...")
        self.hechizos = self.load_json("hechizos.json")
        print("OK!")
        print("Cargando Objetos.json")
        self.hechizos = self.load_json("objetos.json")
        print("OK!")


    def agregar_cliente(self, clientes):
        self.clientes.append(clientes)

    def agregar_comando(self, cliente, comando): 
        # Agrega un comando a la 
        self.cola_comandos.put((cliente, comando))

    def load_json(self, file_name):
        # Retorna una lista con los objetos del JSON [{id:0, name: asd}, {id:1 , name : dsa}]
        path = "./Archivos/" + file_name
        try:
            with open(path, "r") as file:
                data = json.load(file)
        except Exception as e:
            print("Sucedio un error leyendo el archivo " + path)
            print (e)
        
        return data


    def get_client_index(self,socket_id):
        # Dado un socket id -> devuelve un el cliente <object>
        found_index = -1
        for i in range (0,len(self.clientes)):
            if self.clientes[i].soy_socket(socket_id):
                found_index = self.clientes[i]
        return found_index


    def agregar_personaje(self, comando, cliente):
        comando = comando.split(";!:")
        usuario = comando[1]
        contraseña = comando[2]
        print("Ingresando personaje en el mundo")
        print(usuario)
        print(contraseña)
        # If user in db
        # Get user info
        # Then
        aux = Personaje()
        cliente.set_personaje(aux)
        print("Personaje cargado en el mundo")
        print(self.clientes[0].get_personaje())     

    def procesar_comandos(self):
        while self.server_on:
            print("Servidor analizando paquete..")
            cliente, comando = self.cola_comandos.get() #Recibe el cliente del juego y el comando enviado
            if str(comando).split(";!:")[0] == "b'login":
                self.agregar_personaje(str(comando), cliente)
            # procesar comando y actualizar estado del juego
