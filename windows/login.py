# login.py (fix rápido)
from PySide6.QtUiTools import QUiLoader 
from PySide6.QtCore import QFile, QIODevice
from data.usuario import UsuarioData
from windows.main import MainWindow
from model.usuario import Usuario
from resources import imagenes_rc
from PySide6.QtWidgets import QMessageBox, QApplication, QWidget
import sys

class Login(QWidget):    # si tu .ui es un QWidget
    def __init__(self):
        super().__init__()
        ui_file_name = "gui/login.ui"
        ui_file = QFile(ui_file_name)
        if not ui_file.open(QIODevice.ReadOnly):
            raise FileNotFoundError(ui_file_name)
        loader = QUiLoader()
        self.login = loader.load(ui_file, None)   # sin parent -> toplevel del .ui
        ui_file.close()

        # si loader.load devolvió el widget toplevel, lo mostramos
        self.login.lblMensaje.setText("")
        self.login.btnIngresar.clicked.connect(self.ingresar)
        self.login.show()

    def ingresar(self):
        if len(self.login.txtUsuario.text()) < 2:
            self.login.lblMensaje.setText("Ingrese un usuario válido")
            self.login.txtUsuario.setFocus()
            return
        if len(self.login.txtClave.text()) < 3:
            self.login.lblMensaje.setText("Ingrese una contraseña válida")
            self.login.txtClave.setFocus()
            return

        usu = Usuario(usuario=self.login.txtUsuario.text(), clave=self.login.txtClave.text())
        res = UsuarioData().login(usu)
        if res:
            # crea y muestra correctamente la ventana principal
            self.main = MainWindow()
            self.main.showMaximized()   # mostrar la instancia QMainWindow
            self.login.close()          # cerrar el login
        else:
            self.login.lblMensaje.setText("Datos de acceso incorrectos")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = Login()
    sys.exit(app.exec())
