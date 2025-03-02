import sys
from PyQt5 import QtWidgets

import Plantilla_Grafica
import matplotlib.pyplot as plt

import Plantilla_Grafica as interfaz

class MyApp(QtWidgets.QMainWindow, interfaz.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        interfaz.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los Signals
        self.btn_graficar.clicked.connect(self.graficar)
        # VALORES POR DEFECTO
        self.configuracion = {
            "estilo": ":",
            "color_linea": "black",
            "ancho_Linea": 1
        }
        self.limite = {
            "x": [1, 10, 10],  # min, max, divisiones
            "y": [1, 10, 10]   # min, max, divisiones
        }

        #Area de los Slots

    def graficar(self):
        polinomio = self.txt_polinomio.text()   # Ej: 2x^2+3x+4
        polinomio = polinomio.replace("^","**") # 2x**2+3x+4

        #tabular... valores de X con base en los cuales pueda obtener los valores de y
        X = [i for i in range(self.limite["x"][0], self.limite["x"][1])] # Lista de Comprension
        print("Valores de X: ")
        print(X)

        #y = polinomio.replace("x","*("+str(x[0])+")") #2*(X[0])**2+3*(X[0])+4
        y = [eval(polinomio.replace("x","*("+str(x)+")")) for x in X]
        print("Valores de Y: ")
        print(y)

        self.ax.plot(X, y,
                linestyle= self.configuracion["estilo_linea"], #: - -- -
                color= self.configuracion["color_linea"], # tamaño de la linea
                linewidth= self.configuracion["ancho_linea"], # tamaño de la linea
                marker=".", # o . * x 1
                markersize=4,
                makerfacecolor="yellow", # color interno del marcador
                markeredgewidth=1, # tamaño del border del macador
                markeredcolor="blue", # colo del borde del marcador
                dash_capstyle="butt", # dash or solid : "butt" "round" "projecting"
                dash_joinstyle="miter" # dash o solid : "rounf" "bevel"
                )

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())