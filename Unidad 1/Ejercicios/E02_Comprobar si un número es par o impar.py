import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E02_Comprobar si un número es par o impar.ui"
UI_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, UI_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        UI_MainWindow.__init__(self)
        self.setupUi(self)
        self.btn_revisar.clicked.connect(self.par)

    def par(self):
        try:
            num = float(self.txt_numero.toPlainText())
            if num % 2 == 0:
                self.msg("El Número es Par.")
            else:
                self.msg("El Número No es Par.")
        except ValueError:
            self.msg("Por favor Ingresa un Número Válido.")

    def msg(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
