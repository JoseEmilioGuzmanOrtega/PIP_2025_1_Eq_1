import sys
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "PP02_SimularReloj.ui"  # nombre del archivo aquí
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_temporizador.clicked.connect(self.iniciarTempo)
        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.relojV2)

        # Área de los Slots
    def iniciarTempo(self):
        self.horas = int(self.txt_horas.text())
        self.minutos = int(self.txt_minutos.text())
        self.segundos = int(self.txt_segundos.text())
        self.segundoPlano.start(1000)   

    def relojV2(self):

        self.segundos += 1

        if self.segundos == 60:
            self.segundos = 0
            self.minutos += 1

        if self.minutos == 60:
            self.minutos = 0
            self.horas += 1

        if self.horas == 24:
            self.horas = 0

        self.txt_segundos.setText(f"{self.segundos:02d}")
        self.txt_minutos.setText(f"{self.minutos:02d}")
        self.txt_horas.setText(f"{self.horas:02d}")

    def temporizador(self):
        import time as t
        valor = int(self.txt_segundos.text())

        for v in range(valor, 0, -1):
            self.txt_horas.setText(str(v))
            print(v)
            t.sleep(0.25)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
