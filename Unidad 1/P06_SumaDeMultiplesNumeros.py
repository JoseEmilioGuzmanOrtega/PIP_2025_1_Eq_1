import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P06_SumaDeMultiplesNumeros.ui" #nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los Signals
        self.btn_agregar.clicked.connect(self.agregar)
        self.btn_guardar.clicked.connect(self.guardar)
        self.numeros = [] #lista vacia, puede ser utilizada en cualquier parte de la clase

        #Area de los Slots
    def agregar(self):
        num = float(self.txt_numero.text())
        self.numeros.append(num)
        self.sumar()

    def guardar(self):
        archivo = open("../Archivos/numeros.csv","w") # "w" = write / "a" = append
        for num in self.numeros:
            archivo.write(str(num) + "\n")
        archivo.flush()
        archivo.close()
        self.msg("Archivo Guardado! :D")

    def sumar(self):
        sumaaa = sum(self.numeros)
        self.txt_suma.setText(str(sumaaa))

    def msg(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())