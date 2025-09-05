from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice

from gui.registro import RegistroWindow
from resources import imagenes_rc
from PySide6.QtWidgets import QMessageBox

class MainWindow():
    def __init__(self):
        ui_file_name = "gui/main.ui"
        ui_file = QFile(ui_file_name)
        loader = QUiLoader()

        self.main = loader.load(ui_file)

        self.initGUI()
        self.main.showMaximized()
    def initGUI(self):
        self.main.btnRegistrar_Transferencias.triggered.connect(self.abrirRegistro)
        

    def abrirRegistro(self):
        self.registro1 = RegistroWindow()
        self.registro1.v.btnRegistrar.clicked.connect(self.registrarTransaccion)
        self.registro1

    def registrarTransaccion(self):
        if self.registro1.v.cbTipo.currentText() == "--- Seleccione una opción":
            mBox = QMessageBox()
            mBox.setText("Debe seleccionar un tipo de documento")
            mBox.exec()
        elif len(self.registro1.v.txtDocumento.text())<4:
            mBox = QMessageBox()
            mBox.setText("Debe ingresar un documento válido")
            mBox.exec()
        elif self.registro1.v.cbMotivo.currentText() == "--- Seleccione una opción":
            mBox = QMessageBox()
            mBox.setText("Debe seleccionar el motivo")
            mBox.exec()
        elif not self.registro1.v.txtMonto.text().isnumeric():
            mBox = QMessageBox()
            mBox.setText("Debe ingresar un monto válido")
            mBox.exec()
