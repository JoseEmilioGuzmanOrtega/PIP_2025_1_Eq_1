import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P03_EjemploDial.ui" #nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los Signals
        self.dial.valueChanged.connect(self.cambiarValor)
        self.dial.setMinimum(-10)
        self.dial.setMaximum(10)
        self.dial.setSingleStep(2)
        self.dial.setValue(0)

        #Area de los Slots
    def cambiarValor(self):
        valor = str(self.dial.value())
        self.lineEdit.setText(valor)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
