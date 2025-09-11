from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice

from windows.registro import RegistroWindow
from windows.ventas_window import RegistroVenta
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
        self.main.btnVentas.triggered.connect(self.abrirVentas)
        

    def abrirRegistro(self):
        self.registro1 = RegistroWindow()
        self.registro1.submitted.connect(self.onRegistroSubmitted)
        self.registro1.show()
    
    def onRegistroSubmitted(self, data):
        # aquí procesas/guardas/actualizas UI principal
        QMessageBox.information(self.main, "OK", f"Registro recibido: {data}")
        # ejemplo: actualizar tabla en main, etc.

    #Registro de ventas
    def abrirVentas(self):
        self.registroVenta = RegistroVenta()
        self.registroVenta.show()

    
