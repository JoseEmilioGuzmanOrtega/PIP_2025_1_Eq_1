import sys
import random
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "simondice.ui" #nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.secuencia = []
        self.index_secuencia = 0
        self.datosImagenes = {
            "santo": self.lbl_santo,
            "raton": self.lbl_raton,
            "kirby": self.lbl_kirby,
            "angelito": self.lbl_angelito,
        }
        self.datosBotones = {
            "santo": self.btn_santo,
            "raton": self.btn_raton,
            "kirby": self.btn_kirby,
            "angelito": self.btn_angelito,
        }

        self.btn_santo.clicked.connect(lambda: self.check_answer("santo"))
        self.btn_raton.clicked.connect(lambda: self.check_answer("raton"))
        self.btn_kirby.clicked.connect(lambda: self.check_answer("kirby"))
        self.btn_angelito.clicked.connect(lambda: self.check_answer("angelito"))

        self.iniciar_juego()

    def iniciar_juego(self):
        self.secuencia = []
        self.index_secuencia = 0
        self.agregar_color_a_secuencia()
        self.mostrar_secuencia()

    def agregar_color_a_secuencia(self):
        color_aleatorio = random.choice(list(self.datosImagenes.keys()))
        self.secuencia.append(color_aleatorio)

    def mostrar_secuencia(self):
        self.index_secuencia = 0
        self.label.setText("Observa la Secuencia...")
        QtCore.QTimer.singleShot(1000, self.reproducir_secuencia)

    def reproducir_secuencia(self):
        if self.index_secuencia < len(self.secuencia):
            color = self.secuencia[self.index_secuencia]
            self.label.setText(f"{self.index_secuencia + 1}. {color}")
            self.datosImagenes[color].setStyleSheet("background-color: green;")
            QtCore.QTimer.singleShot(500, self.apagar_color)
        else:
            self.label.setText("Tu turno: Repítela.")
            self.index_secuencia = 0

    def apagar_color(self):
        color = self.secuencia[self.index_secuencia]
        self.datosImagenes[color].setStyleSheet("background-color: none;")
        self.index_secuencia += 1
        QtCore.QTimer.singleShot(500, self.reproducir_secuencia)

    def check_answer(self, color):
        if self.index_secuencia < len(self.secuencia) and self.secuencia[self.index_secuencia] == color:
            self.datosImagenes[color].setStyleSheet("background-color: green;")
            self.index_secuencia += 1
            if self.index_secuencia == len(self.secuencia):
                QtCore.QTimer.singleShot(500, self.nueva_ronda)
        else:
            self.label.setText("Incorrecto. Reiniciando el Juego...")
            self.datosImagenes[color].setStyleSheet("background-color: red;")

            QtCore.QTimer.singleShot(1000, self.reiniciar_juego)

    def nueva_ronda(self):
        self.reset_colores()
        self.agregar_color_a_secuencia()
        self.mostrar_secuencia()

    def reset_colores(self):
        for label in self.datosImagenes.values():
            label.setStyleSheet("background-color: none;")

    def reiniciar_juego(self):
        self.reset_colores()
        self.label.setText("Reiniciando Juego...")
        QtCore.QTimer.singleShot(1000, self.iniciar_juego)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
