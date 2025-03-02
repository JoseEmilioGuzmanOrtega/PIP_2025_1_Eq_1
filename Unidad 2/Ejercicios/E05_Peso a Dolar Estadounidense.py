import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E05_Peso a Dolar Estadounidense.ui"  # Nombre del archivo UI
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.spinBox.setMinimum(0)
        self.spinBox.setMaximum(100000)
        self.spinBox.setSingleStep(1)
        self.spinBox.setValue(0)
        self.spinBox.valueChanged.connect(self.cambiaValor)

    def cambiaValor(self):
        MX = self.spinBox.value()  
        dolar = MX / 21
        self.label_dolar.setText(f"${dolar:.2f}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
