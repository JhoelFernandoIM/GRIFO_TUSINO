from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice

from windows.registro import RegistroWindow
from windows.turnos_window import GestionTurno
from windows.ventas_window import RegistroVenta
from resources import imagenes_rc
from PySide6.QtWidgets import QMessageBox, QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        ui_file_name = "gui/main.ui"
        ui_file = QFile(ui_file_name)
        loader = QUiLoader()

        self.main = loader.load(ui_file, self)

        self.initGUI()
        self.main.showMaximized()

    def initGUI(self):
        self.main.btnPrincipal.triggered.connect(self.volverPrincipal)
        self.main.btnRegistrar_Transferencias.triggered.connect(self.abrirRegistro)
        self.main.btnVentas.triggered.connect(self.abrirVentas)
        self.main.btnTurnos.triggered.connect(self.abrirTurnos)
        

#aqui ponemos las funciones que instancian cada modulo para ejecutarlos

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
        self.registroVenta = RegistroVenta(self.main)
        self.registroVenta.show()

    #Abrir stacked widget: turno
    def abrirTurnos(self):
        self.gestionTurno = GestionTurno(self.main.stackedWidget)
        self.gestionTurno.show()

    #Volver principal
    def volverPrincipal(self):
        self.page_index = 0
        self.main.stackedWidget.setCurrentIndex(self.page_index)


    
