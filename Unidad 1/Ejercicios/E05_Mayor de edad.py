import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E05_Mayor de edad.ui"
UI_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, UI_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        UI_MainWindow.__init__(self)
        self.setupUi(self)
        self.btn_calcular.clicked.connect(self.edad )

    def edad(self):
        try:
            edad = float(self.txt_edad.text())
            if 18 < edad:
                self.mensaje ("Es Mayor de Edad")
            else:
              self.mensaje ("No es Mayor de Edad")


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

