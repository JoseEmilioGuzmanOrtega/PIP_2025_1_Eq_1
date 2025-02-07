import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P08_CarruselImagenes.ui" #nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los Signals
        self.selector_imagen.valueChanged.connect(self.cambiarValor)
        self.selector_imagen.setMinimum(0)
        self.selector_imagen.setMaximum(9)
        self.selector_imagen.setSingleStep(0)
        self.selector_imagen.setValue(1)

        self.datosImagenes = {
            0: [":/Fotos/mew.jpg", "mew"],
            1: [":/Fotos/celinemuerta.jpg", "celinemuerta"],
            2: [":/Fotos/dennisse.jpg", "dennisse"],
            3: [":/Fotos/yoshi.jpg", "yoshi"],
            4: [":/Fotos/pikachu.jpg", "pikachu"],
            5: [":/Fotos/raton.jpg", "raton"],
            6: [":/Fotos/santo.jpg", "santo"],
            7: [":/Fotos/angelito.jpg", "angelito"],
            8: [":/Fotos/goyo.jpg", "goyo"],
            9: [":/Fotos/buenosdias.jpg", "buenosdias"]
        }

        #Area de los Slots
    def cambiarValor(self):
        valor = self.selector_imagen.value()
        imagen_ruta = self.datosImagenes[valor][0]
        self.imagen.setPixmap(QtGui.QPixmap(imagen_ruta))
        print(valor)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
