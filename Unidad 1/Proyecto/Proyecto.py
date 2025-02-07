import statistics
import sys
from PyQt5 import uic, QtWidgets
from numpy.ma.extras import median

qtCreatorFile = "Proyecto.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setFixedSize(850, 600)
        self.btn_agregar.clicked.connect(self.agregar)
        self.btn_cargar.clicked.connect(self.cargar)
        self.btn_cargar.clicked.connect(self.resultados)
        self.btn_guardar.clicked.connect(self.guardar)
        self.numeros = []  # lista vacia, puede ser utilizada en cualquier parte de la clase

    def cargar(self):
        archivo = open("../Archivos/numeros.csv")
        contenido = archivo.readlines()
        archivo.close()

        nums = []
        for i in contenido:
            try:
                nums.append(float(i.strip()))  # Intentar convertir solo los números
            except ValueError:
                pass  # Ignorar líneas que no sean números

        self.numeros = nums
        self.txt_lista_numeros.setText(str(self.numeros))
        self.resultados()  # Para actualizar los cálculos con los datos cargados

    def agregar(self):
        try:
            num = float(self.txt_numero.text())
            self.numeros.append(num)
            self.txt_lista_numeros.setText(str(self.numeros))
            self.txt_numero.clear()
            self.resultados()  # Se mueve aquí para actualizar en automático
        except Exception as error:
            print(error)

    def guardar(self):
        archivo = open("../Archivos/numeros.csv","w")  # "w" = write / "a" = append
        for num in self.numeros:
            archivo.write(str(num) + "\n")
            archivo.write("Minimo: " + str(min(self.numeros)) + "\n")
            archivo.write("Maximo: " + str(max(self.numeros)) + "\n")
            archivo.write("Media: " + str(sum(self.numeros) / len(self.numeros)) + "\n")
            archivo.write("Varianza: " + str(self.varianza()) + "\n")
            archivo.write("Desviacion: " + str(self.desviacion()) + "\n")
            archivo.write("Mediana: " + str(self.mediana()) + "\n")
        archivo.flush()
        archivo.close()
        self.msg("Archivo Guardado! :D")



    def resultados(self):
        minimo = min(self.numeros)
        maximo = max(self.numeros)
        media = sum(self.numeros) / len(self.numeros)
        varianza = self.varianza()
        desviacion = self.desviacion()
        mediana = self.mediana()
        moda = statistics.mode(self.numeros)

        # Asignar los valores a los elementos de la interfaz
        self.txt_valor_menor.setText(str(minimo))
        self.txt_valor_mayor.setText(str(maximo))
        self.txt_Media.setText(str(media))
        self.txt_Varianza.setText(str(varianza))
        self.txt_Desviacion.setText(str(desviacion))
        self.txt_Mediana.setText(str(mediana))
        self.txt_Moda.setText(str(moda))

    def varianza(self):
        media = sum(self.numeros) / len(self.numeros)
        suma_cuadrados = sum((x - media) ** 2 for x in self.numeros)
        varianza = suma_cuadrados / len(self.numeros)
        return varianza

    def mediana(self):
        ordenado = sorted(self.numeros)
        n = len(self.numeros)
        if n % 2 == 0:
            mediana = (ordenado[(n // 2) - 1] + ordenado[n // 2]) / 2
        else:
            mediana = ordenado[n // 2]
        return mediana

    def desviacion(self):
        varianza = self.varianza()
        desviacion_estandar = (varianza ** 0.5)
        return desviacion_estandar

    def msg(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())