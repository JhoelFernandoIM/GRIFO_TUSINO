from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice
from data.usuario import UsuarioData
from windows.main import MainWindow
from model.usuario import Usuario
from resources import imagenes_rc
from PySide6.QtWidgets import QMessageBox

class Login():
    def __init__(self):
        ui_file_name = "gui/login.ui"
        ui_file = QFile(ui_file_name)
        loader = QUiLoader()

        self.login = loader.load(ui_file)

        self.initGUI()
        self.login.lblMensaje.setText("")
        self.login.show()

    def ingresar(self):
        if len(self.login.txtUsuario.text()) < 2:
            self.login.lblMensaje.setText("Ingrese un usuario válido")
            self.login.txtUsuario.setFocus()
        elif len(self.login.txtClave.text()) < 3:
            self.login.lblMensaje.setText("Ingrese una contraseña válida")
            self.login.txtClave.setFocus()
        else:
            self.login.lblMensaje.setText("")
            usu = Usuario(usuario=self.login.txtUsuario.text(), clave=self.login.txtClave.text())
            usuData = UsuarioData()
            res=usuData.login(usu)
            if res:
                self.main = MainWindow()
                self.login.hide()
            else:
                self.login.lblMensaje.setText("Datos de acceso incorrectos") 

    def initGUI(self):
        self.login.btnIngresar.clicked.connect(self.ingresar)