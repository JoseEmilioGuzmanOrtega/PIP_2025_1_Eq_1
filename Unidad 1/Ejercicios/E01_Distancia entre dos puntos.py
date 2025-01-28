import sys
from PyQt5 import uic, QtWidgets
import math

qtCreatorFile = "E01_Distancia entre dos puntos.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_calcular.clicked.connect(self.calcular_distancia)

        self.setWindowTitle("Calculadora de Distancia entre dos puntos")
        self.resize(500, 400)

    def calcular_distancia(self):
        try:
            x1 = float(self.X1.toPlainText())
            y1 = float(self.y1.toPlainText())
            x2 = float(self.x2.toPlainText())
            y2 = float(self.y2.toPlainText())

            distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

            self.labelResultado.setText(f"Resultado: {distancia:.2f}")
        except ValueError:
            self.labelResultado.setText("Por favor ingrese números válidos.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
