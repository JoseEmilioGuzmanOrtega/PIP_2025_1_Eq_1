import sys
from PyQt5 import uic, QtWidgets, QtCore
import serial as placa
import time

qtCreatorFile = "Practica4_ArduinoPythonGUI_ReadWrite_ListWidget_Boton.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.arduino = None
        self.recibir_sensor0 = True
        self.recibir_sensor1 = True
        self.recibir_sensor2 = True

        self.btn_accion.clicked.connect(self.accion)

        self.btn_led0.clicked.connect(self.control_led0)
        self.btn_led0.setText("Prender")

        self.btn_led1.clicked.connect(self.control_led1)
        self.btn_led1.setText("Prender")

        self.btn_led2.clicked.connect(self.control_led2)
        self.btn_led2.setText("Prender")

        if not hasattr(self, 'lista_datos'): print("Advertencia: 'lista_datos' no encontrado en UI.")
        if not hasattr(self, 'lista_datos_2'): print("Advertencia: 'lista_datos_2' no encontrado en UI.")
        if not hasattr(self, 'lista_datos_3'): print("Advertencia: 'lista_datos_3' no encontrado en UI.")


        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.lecturas)

    def accion(self):
        texto = self.btn_accion.text().upper()
        if texto == "CONECTAR":
            com = "COM" + self.txt_com.text()
            self.btn_accion.setText("DESCONECTAR")
            self.txt_estado.setText("CONECTADO")
            self.arduino = placa.Serial(com, baudrate=9600, timeout=1)
            self.lista_datos.clear()
            self.lista_datos_2.clear()
            self.lista_datos_3.clear()
            time.sleep(1.5)
            self.segundoPlano.start(100)
        elif texto == "DESCONECTAR":
            self.btn_accion.setText("RECONECTAR")
            self.txt_estado.setText("DESCONECTADO")
            if self.segundoPlano.isActive():
                self.segundoPlano.stop()
            if self.arduino and self.arduino.isOpen():
                self.arduino.close()
        else:
            self.btn_accion.setText("DESCONECTAR")
            self.txt_estado.setText("RECONECTADO")
            if self.arduino:
                self.arduino.open()
                self.lista_datos.clear()
                self.lista_datos_2.clear()
                self.lista_datos_3.clear()
                time.sleep(1.5)
                self.segundoPlano.start(100)


    def lecturas(self):
        if self.arduino and self.arduino.isOpen() and self.arduino.inWaiting() > 0:
            lectura_bytes = self.arduino.readline()
            lectura = lectura_bytes.decode('utf-8', errors='ignore').replace('\x00', '').strip()

            if lectura:
                partes = lectura.split('@')
                if partes[-1] == '':
                    partes = partes[:-1]

                if len(partes) == 3:
                    valores_int = [int(p) for p in partes]

                    if self.recibir_sensor0:
                        self.lista_datos.addItem(f"{valores_int[0]}")
                        self.lista_datos.setCurrentRow(self.lista_datos.count() - 1)

                    if self.recibir_sensor1:
                        self.lista_datos_2.addItem(f"{valores_int[1]}")
                        self.lista_datos_2.setCurrentRow(self.lista_datos_2.count() - 1)

                    if self.recibir_sensor2:
                        self.lista_datos_3.addItem(f"{valores_int[2]}")
                        self.lista_datos_3.setCurrentRow(self.lista_datos_3.count() - 1)


    def control_led0(self):
        self.recibir_sensor0 = not self.recibir_sensor0
        if self.recibir_sensor0:
            self.btn_led0.setText("Prender")
        else:
            self.btn_led0.setText("Apagar")


    def control_led1(self):
        self.recibir_sensor1 = not self.recibir_sensor1
        if self.recibir_sensor1:
            self.btn_led1.setText("Prender")
        else:
            self.btn_led1.setText("Apagar")


    def control_led2(self):
        self.recibir_sensor2 = not self.recibir_sensor2
        if self.recibir_sensor2:
            self.btn_led2.setText("Prender")
        else:
            self.btn_led2.setText("Apagar")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())