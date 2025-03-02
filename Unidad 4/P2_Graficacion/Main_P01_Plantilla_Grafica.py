import sys
from PyQt5 import uic, QtWidgets

#qtCreatorFile = "P4_ChecarPuedeVotar.ui" #nombre del archivo aqui
#Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

import Plantilla_Grafica as interfaz

class MyApp(QtWidgets.QMainWindow, interfaz.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        interfaz.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los Signals
        self.btn_comprobar.clicked.connect(self.comprobar)

        #Area de los Slots
    def comprobar(self):
        edad = int(self.txt_edad.text())
        if edad >= 18:
            self.msg("Puedes Votar :D")
        else:
            self.msg("No Puedes Votar :C")

    def msg(self, mensaje):
        m = QtWidgets.QMessageBox()
        m.setText(mensaje)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())