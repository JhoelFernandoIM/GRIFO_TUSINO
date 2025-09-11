from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, QObject, Signal


from PySide6.QtWidgets import QMessageBox

class RegistroVenta(QObject):
    submitted = Signal(dict)  # emite un dict con los datos validados

    def __init__(self, parent=None):
        super().__init__(parent)

        ui_file_name = "gui/ventas_window.ui"
        ui_file = QFile(ui_file_name)

        if not ui_file.open(QIODevice.ReadOnly):
            raise RuntimeError(f"No se puede abrir {ui_file_name}")

        loader = QUiLoader()
        self.v = loader.load(ui_file)
        ui_file.close()

        # Conectar el botón internamente para mantener responsabilidad en este módulo
        self.v.btnRegistrarVenta.clicked.connect(self.registrarVenta)

        # si se pasa un callback, lo conectamos al botón


    def show(self):
        self.v.show()

    def registrarVenta(self):
        if self.v.cmbCliente.currentText() == "--- Seleccione una opción":
            mBox = QMessageBox()
            mBox.setText("Debe seleccionar un cliente de la lista")
            mBox.exec()
        elif self.v.cmbSurtidor.currentText() == "--- Seleccione una opción":
            mBox = QMessageBox()
            mBox.setText("Debe seleccionar un Surtidor disponible")
            mBox.exec()
        elif self.v.cmbMetodoPago.currentText() == "--- Seleccione una opción":
            mBox = QMessageBox()
            mBox.setText("Debe seleccionar un Método de pago de la lista")
            mBox.exec()

        data = {
            "cliente": self.v.cbTipo.currentText(),
            "surtidor": self.v.txtDocumento.text(),
            "metodo": self.v.cbMotivo.currentText(),
            "litro": self.v.txtLitros.text(),
            "monto": float(self.v.txtMonto.text()),
            # agrega lo que necesites
        }
        # emite para que main (u otro) lo procese
        self.submitted.emit(data)
