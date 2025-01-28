import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E07_Cadena.ui"
UI_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, UI_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        UI_MainWindow.__init__(self)
        self.setupUi(self)
        self.btn_calcular.clicked.connect(self.cadena)

    def cadena(self):
        try:
            ncadena = len(self.txt_cadena.text())

            self.mensaje("El Número de Caracteres es: " + str(ncadena))
        except Exception as error:
            print(error)

    def mensaje(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
