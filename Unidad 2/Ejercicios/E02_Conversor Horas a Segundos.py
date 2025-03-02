import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E02_Conversor Horas a Segundos.ui"  # Nombre del archivo UI
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.dial.setMinimum(0)
        self.dial.setMaximum(23)
        self.dial.setSingleStep(1)
        self.dial.valueChanged.connect(self.cambiarvalor)

    def cambiarvalor(self, valor):
        hora = self.dial.value()
        segundos = hora * 3600
        self.label_hora.setText(f"Hora: {hora}:00")
        self.label_resultado.setText(f"Segundos del Día: {segundos}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
