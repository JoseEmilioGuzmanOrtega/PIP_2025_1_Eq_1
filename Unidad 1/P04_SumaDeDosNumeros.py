import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P04_SumaDeDosNumeros.ui" #nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los Signals
        self.btn_sumar.clicked.connect(self.suma)

        #Area de los Slots
    def suma(self):
            try:
                num1 = float(self.txt_A.text())
                num2 = float(self.txt_B.text())
                #print("Hola")
                sum= num1 + num2
                self.msg("La suma de los numeros es: " + str(sum))
            except Exception as error:
                  print(error)

    def msg(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())