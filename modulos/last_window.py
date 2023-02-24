import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit)
from PyQt6.QtGui import QFont
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit

class last_window(QWidget):

    def __init__(self):
        super().__init__()
        self.iniciarUI()

    def iniciarUI(self):
        self.setGeometry(100,100,250,340)
        self.setWindowTitle("last_window")
        self.setStyleSheet("background-color: white;")
        self.configurarVentanaConImagen()
        self.show()

    def configurarVentanaConImagen(self):
        mensaje_rotulo = QLabel(self)
        mensaje_rotulo.setText(" Su producto ha sido adquirido con éxito \n será despachado en los siguientes días\n gracias por su compra")
        mensaje_rotulo.move(15,15)
        ##img
        imagen = "img/logoo.jpg"

        ##boton
        boton_cerrar = QPushButton("Cerrar", self)
        boton_cerrar.move(90,300)
        boton_cerrar.clicked.connect(self.close)
        boton_cerrar.setStyleSheet('background-color: #DCFFF9;')
        

        try:
            with open(imagen):
                logo_final = QLabel(self)
                pixmap = QPixmap(imagen)
                logo_final.setPixmap(pixmap)
                logo_final.move(25,80)
        except FileNotFoundError as error:
            print(f"Imagen no encontrada.\nError: {error}")


if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    ventana = last_window()
    sys.exit(aplicacion.exec())
