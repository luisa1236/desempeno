
from com.apuntes.poo.Persona import Persona

class estudiante(Persona):

    def __init__(self, id, nombre, correo,contrasena, programa, semestre):
        super().__init__(id, nombre, correo, contrasena)
        self.programa = programa
        self.semestre = semestre

    def verPersona(self):
        print(f"id:{self.id} \n ",
              f"nombre:{self.nombre} \n",
              f"correo:{self.correo} \n",
              f"compañia:{self.compañia} \n",
              f"programa:{self.programa} \n",
              f"semestre:{self.semestre} \n")

estudiante1 = estudiante(1, "Maria", "mail.com", "123456", "Desarrollo", 1)

print(estudiante1.programa)
