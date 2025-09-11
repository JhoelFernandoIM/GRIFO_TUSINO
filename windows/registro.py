from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, QObject, Signal

from model.usuario import Usuario
from resources import imagenes_rc
from PySide6.QtWidgets import QMessageBox

class RegistroWindow(QObject):
    submitted = Signal(dict)  # emite un dict con los datos validados

    def __init__(self, parent=None):
        super().__init__(parent)

        ui_file_name = "gui/registro.ui"
        ui_file = QFile(ui_file_name)

        if not ui_file.open(QIODevice.ReadOnly):
            raise RuntimeError(f"No se puede abrir {ui_file_name}")

        loader = QUiLoader()
        self.v = loader.load(ui_file)
        ui_file.close()

        # Conectar el botón internamente para mantener responsabilidad en este módulo
        self.v.btnRegistrar.clicked.connect(self.registrarTransaccion)

        # si se pasa un callback, lo conectamos al botón


    def show(self):
        self.v.show()

    def registrarTransaccion(self):
        if self.v.cbTipo.currentText() == "--- Seleccione una opción":
            mBox = QMessageBox()
            mBox.setText("Debe seleccionar un tipo de documento")
            mBox.exec()
        elif len(self.v.txtDocumento.text())<4:
            mBox = QMessageBox()
            mBox.setText("Debe ingresar un documento válido")
            mBox.exec()
        elif self.v.cbMotivo.currentText() == "--- Seleccione una opción":
            mBox = QMessageBox()
            mBox.setText("Debe seleccionar el motivo")
            mBox.exec()
        elif not self.v.txtMonto.text().isnumeric():
            mBox = QMessageBox()
            mBox.setText("Debe ingresar un monto válido")
            mBox.exec()

        data = {
            "tipo": self.v.cbTipo.currentText(),
            "documento": self.v.txtDocumento.text(),
            "motivo": self.v.cbMotivo.currentText(),
            "monto": float(self.v.txtMonto.text()),
            # agrega lo que necesites
        }
        # emite para que main (u otro) lo procese
        self.submitted.emit(data)
