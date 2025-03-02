import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E06_Area de un Pentagono.ui"  # Nombre del Archivo UI
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_resolver.clicked.connect(self.calcular_area)

        for spin in [self.spin_lado1, self.spin_lado2, self.spin_lado3, self.spin_lado4, self.spin_lado5]:
            spin.setMinimum(0)
            spin.setMaximum(1000)
            spin.setSingleStep(1)
            spin.setValue(0)

    def calcular_area(self):
        lados = [self.spin_lado1.value(),
                 self.spin_lado2.value(),
                 self.spin_lado3.value(),
                 self.spin_lado4.value(),
                 self.spin_lado5.value()]
        perimetro = sum(lados)
        apotema = lados[0] / (2 * (3.1416 / 5))
        area = (perimetro * apotema) / 2
        self.label_3.setText(f"Área aproximada: {area:.2f}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
