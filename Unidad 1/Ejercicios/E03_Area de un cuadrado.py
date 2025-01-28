import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E03_Area de un cuadrado.ui"
UI_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, UI_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        UI_MainWindow.__init__(self)
        self.setupUi(self)
        self.btn_calcular.clicked.connect(self.area)

    def area(self):
        try:
            num1 = float(self.txt_A.text())

            area = num1 * num1
            self.mensaje("El Area del Cuadrado es  "+str(area))
        except Exception as error:
            print(error)

    def mensaje(self, txt):
        m=QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

