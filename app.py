from PySide6.QtWidgets import QApplication

from windows.login import Login

import sys

#Creando la clase Grifo
class Grifo():
    def __init__(self):
        self.app = QApplication(sys.argv) #Crea la aplicacion para cada objeto que se instancia de esta clase
        self.login = Login()

        self.app.exec() #Ejecuta la aplicación

#Instanciamos la app de la clase Grifo
if __name__ == "__main__":
    app = Grifo()