import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E07_Teorema de Pitagoras.ui"  # Nombre del archivo UI
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.spin_A.setMinimum(0)
        self.spin_A.setMaximum(10000)
        self.spin_A.setSingleStep(1)
        self.spin_A.setValue(0)
        self.spin_A.valueChanged.connect(self.teorema)

        self.spin_B.setMinimum(0)
        self.spin_B.setMaximum(10000)
        self.spin_B.setSingleStep(1)
        self.spin_B.setValue(0)
        self.spin_B.valueChanged.connect(self.teorema)

    def teorema(self):
        a = self.spin_A.value()
        b = self.spin_B.value()
        c=a**2+b**2
        calculo=c**0.5
        self.label_3.setText(str(calculo))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
