import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E08_Tabla de Multiplicar.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de los Signals
        self.horizontalSlider.valueChanged.connect(self.tabla)
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(10)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setValue(1)

        #Area de los Slots
    def tabla(self):
        tabla = self.horizontalSlider.value()
        resultado = ""
        for i in range(1, 11):
            resultado += f"{tabla} x {i} = {tabla * i}\n"
        self.label_tabla.setText(resultado)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
