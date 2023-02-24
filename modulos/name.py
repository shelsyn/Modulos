import sys
import sqlite3
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit)
from modulos.last_window import last_window

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
        QLabel(" Estimado cliente, para continuar \n ingrese sus datos ", self).move(10, 10)
        numero1 = QLabel("Nombre", self)
        numero1.move(10, 50)
        self.campo_numero_1 = QLineEdit(self)
        self.campo_numero_1.resize(210, 30)
        self.campo_numero_1.move(70, 50)

        ##botonnn

        aceptar_boton = QPushButton("Siguiente", self)
        aceptar_boton.setStyleSheet('background-color: #DCFFF9;')
        aceptar_boton.move(150, 100)
        aceptar_boton.setEnabled(False)  
        aceptar_boton.clicked.connect(self.ejecutarOperacion)
        
        self.campo_numero_1.textChanged.connect(self.actualizarBoton)  
        self.boton_siguiente = aceptar_boton

        # Conexión a la base de datos y creación de la tabla

        self.conexion = sqlite3.connect("nombres.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS nombres (id INTEGER PRIMARY KEY, nombre TEXT)")

    def actualizarBoton(self):
        if self.campo_numero_1.text():
            self.boton_siguiente.setEnabled(True)  # Activar el botón 
        else:
            self.boton_siguiente.setEnabled(False)  # Desactivar 

    def ejecutarOperacion(self):

         # codigo moduloo

        self.hide()  # se borra el modulo
        self.otro_modulo = last_window()  # modulo (last_window)
        self.otro_modulo.show() 
        print('comprado!')
        nombre = self.campo_numero_1.text()

        # se inserta el nombre en la tabla
        self.cursor.execute("INSERT INTO nombres (nombre) VALUES (?)", (nombre,))
        self.conexion.commit()
        
        print(f"Se ha agregado el nombre {nombre} a la base de datos")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Store()
    sys.exit(app.exec())
