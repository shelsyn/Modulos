import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit)
from PyQt6.QtGui import QFont
class Store(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setMaximumSize(310, 260)
        self.setWindowTitle("Fashion Store")
        self.configurarPantalla()
        self.show()
    def configurarPantalla(self):
        QLabel (" Bienvenido a nuestra pagina web de ropa ", self).move(10, 10) 
        numero1 = QLabel("Ingresa tu \n nombre", self)
        numero1.move(10, 50)
        self.campo_numero_1 = QLineEdit(self)
        self.campo_numero_1.resize(210, 30)
        self.campo_numero_1.move(70, 50)
  
        boton_limpiar = QPushButton("Cancelar", self)
        boton_limpiar.move(50,100)
        #boton_limpiar.clicked.connect(self.clearText)
        aceptar_boton = QPushButton("Siguiente", self)
        aceptar_boton.move(170,100)
        aceptar_boton.clicked.connect(self.ejecutarOperacion)
    def ejecutarOperacion(self):
        x = int(self.campo_numero_1.text())
        print("Siguiente es ", )

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Store()
    sys.exit(app.exec())