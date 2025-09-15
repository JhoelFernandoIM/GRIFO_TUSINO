from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, QObject, Signal


from PySide6.QtWidgets import QMessageBox

class GestionInfraestructura(QObject):
    submitted = Signal(dict)  # emite un dict con los datos validados

    def __init__(self, stacked_widget, parent=None):
        super().__init__(parent)

        self.stacked_widget = stacked_widget

        self.page_index = 2


        # Conectar el botón internamente para mantener responsabilidad en este módulo
        #self.v.btnRegistrarVenta.clicked.connect(self.registrarVenta)

        # si se pasa un callback, lo conectamos al botón


    def show(self):
        self.stacked_widget.setCurrentIndex(self.page_index)

    #def registrarVenta(self): funcion botones, abrir turno, cerrar, etc