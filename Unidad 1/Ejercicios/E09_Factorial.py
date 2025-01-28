import math
import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E09_Factorial.ui"
UI_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, UI_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        UI_MainWindow.__init__(self)
        self.setupUi(self)
        self.btn_boton.clicked.connect(self.factorial)

    def factorial(self):
        try:
            numero = int(self.txt_num.text())
            resultado=math.factorial(numero)
            self.mensaje(f"El Factorial de {numero} es: "+str(resultado))
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