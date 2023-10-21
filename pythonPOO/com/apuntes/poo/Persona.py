

class Persona:

    compania = "xyz"

    def __init__(self,id,nombre,correo,contrasena):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena

    def verPersona(self):
        print(f"id:{self.id} \n ",
              f"nombre:{self.nombre} \n",
              f"correo:{self.correo} \n",
              f"compañia:{self.compania} ")

maria = Persona(1,"Maria","mariaperez@gamail.com","queri1")

maria.verPersona()
