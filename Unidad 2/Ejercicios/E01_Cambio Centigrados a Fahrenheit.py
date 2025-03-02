import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E01_Cambio Centigrados a Fahrenheit.ui"  # Nombre del archivo UI
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.spinBox.setMinimum(-100)
        self.spinBox.setMaximum(100)
        self.spinBox.setSingleStep(1)
        self.spinBox.setValue(0)
        self.spinBox.valueChanged.connect(self.cambiaValor)

    def cambiaValor(self):
        valor = self.spinBox.value()  # Obtener el valor del SpinBox
        fahrenheit = (valor * 9 / 5) + 32  # Conversión
        self.txt_resultado.setText(str(fahrenheit))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
