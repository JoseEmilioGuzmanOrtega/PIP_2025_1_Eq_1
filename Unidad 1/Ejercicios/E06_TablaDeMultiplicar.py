#import sys
#from PyQt5 import uic, QtWidgets

#qtCreatorFile = "E06_TablaDeMultiplicar.ui"
#UI_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

#class MyApp(QtWidgets.QMainWindow, UI_MainWindow):
#    def __init__(self):
#        QtWidgets.QMainWindow.__init__(self)
#        UI_MainWindow.__init__(self)
#        self.setupUi(self)
#        self.btn_calcular.clicked.connect(self.multiplicacion)

#    def multiplicacion(self):
#        try:
#            numero = int(self.txt_num.text())
#            for constante in range(11):
#                resultado: int = numero*constante
#            self.tabla(f"{numero} * {constante} = "+str(resultado))
#        except Exception as error:
#            print(error)

#    def tabla(self, int):
#        m=QtWidgets.QTableView
#        m.setText(int)
#        m.exec_()

#if __name__ == "__main__":
#    app = QtWidgets.QApplication(sys.argv)
#    window = MyApp()
#    window.show()
#    sys.exit(app.exec_())


print("Hola, ¿que tabla de multiplicar deseas saber?")
numero = int(input("Ingresa aqui el numero que quieres: "))
print(f"Tabla de multiplicar del: {numero}")

for constante in range(11):
    resultado: int = numero*constante
    print(f"{numero} * {constante} = {resultado}")