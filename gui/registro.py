from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice

from model.usuario import Usuario
from resources import imagenes_rc
from PySide6.QtWidgets import QMessageBox

class RegistroWindow():
    def __init__(self):
        ui_file_name = "gui/registro.ui"
        ui_file = QFile(ui_file_name)
        loader = QUiLoader()

        self.v = loader.load(ui_file)
        self.v.show()
