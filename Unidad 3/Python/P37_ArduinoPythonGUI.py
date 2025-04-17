import sys
import serial as placa
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P37_ArduinoPythonGUI.ui" #nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los Signals

        self.arduino = None
        self.btn_accion.clicked.connect(self.accion)

        #Area de los Slots

    def accion(self):
        texto = self.btn_accion.text().upper()
        if texto == "CONECTAR": #Inicia la comunicacion y la apertura
            com = "COM" + self.txt_com.text()
            self.btn_accion.setText("DESCONECTAR")
            self.txt_estado.setText("CONECTADO")
            self.arduino = placa.Serial(com, baudrate=9600, timeout=1)
        elif texto == "DESCONECTAR": #Cierra la comunicacion
            self.btn_accion.setText("RECONECTAR")
            self.txt_estado.setText("DESCONECTADO")
            self.arduino.close()
        else: #Reapertura la comunicacion
            self.btn_accion.setText("DESCONECTAR")
            self.txt_estado.setText("RECONECTADO")
            self.arduino.open()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
