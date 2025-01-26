import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "P12_24HRS.ui"
UI_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, UI_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        UI_MainWindow.__init__(self)
        self.setupUi(self)
        self.btn_calcular.clicked.connect(self.reloj)

    def reloj(self):
        try:

            hora = float(self.txt_hora.text())
            resta = 24 - hora
            self.mensaje("Te Quedan " + str(resta) + " Horas")
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
