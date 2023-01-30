import queue
import json

class ControladorJuego:
    def __init__(self):
        self.clientes = [] # Arreglo de instancia de Clientes

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


    def agregar_clientes(self, clientes):
        self.clientes.append(clientes)

    def agregar_comando(self, clientes, comando):
        self.cola_comandos.put((clientes, comando))

    def load_json(self, file_name):
        # Retorna una lista con los objetos del JSON [{id:0, name: asd}, {id:1 , name : dsa}]
        path = "./Archivos/" + file_name
        
        dic_aux ={}
        try:
            with open(path, "r") as file:
                data = json.load(file)
        except Exception as e:
            print("Sucedio un error leyendo el archivo " + path)
            print (e)
        
        return data



        

    def procesar_comandos(self):
        while True:
            clientes, comando = self.cola_comandos.get()
            # procesar comando y actualizar estado del juego
