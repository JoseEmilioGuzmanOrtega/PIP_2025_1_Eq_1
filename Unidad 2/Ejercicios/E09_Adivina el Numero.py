import sys
from PyQt5 import uic, QtWidgets
import random

qtCreatorFile = "E09_Adivina el Numero.ui"  # Nombre del archivo UI
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.spinBox.setMinimum(0)
        self.spinBox.setMaximum(10)
        self.spinBox.setSingleStep(1)
        self.spinBox.setValue(0)
        self.btn_adivinar.clicked.connect(self.adivinar)

        self.numero_actual = random.randint(0, 10)
        self.label_adivinar.setText("¡Intenta adivinar el número!")

    def adivinar(self):
        """Comprueba si el número es correcto y solo cambia si aciertas."""
        if self.spinBox.value() == self.numero_actual:
            self.label_adivinar.setText(f"✅ ¡Correcto! El número era {self.numero_actual}")
            self.numero_actual = random.randint(0, 10)
        else:
            self.label_adivinar.setText(f"❌ Incorrecto, intenta de nuevo.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
