import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit)
from PyQt6.QtGui import QFont
from PyQt6.QtGui import QPixmap; 

class VentanaConImagen(QWidget): 

    def __init__(self): 
        super().__init__(); 
        self.iniciarUI(); 

    def iniciarUI(self): 

        """ Configurar GUI aplicación """ 

        self.setGeometry(100,100,250,340); 

        self.setWindowTitle("Ejemplo con QLabel - Liz Olsen"); 

        self.configurarVentanaConImagen(); 

        self.show(); 

    def configurarVentanaConImagen(self): 
        """ Crear QLabel para ser mostrado en la ventana principal""" 
        mensaje_rotulo = QLabel(self); 
        mensaje_rotulo.setText(" Su producto ha sido adquirido con éxito \n será despachado en los siguientes días\n gracias por su compra"); 
        mensaje_rotulo.move(15,15); 
        imagen = "img/dos.png"; 
        boton_cerrar = QPushButton("Cerrar", self)
        boton_cerrar.move(90,300)
        

        try: 
            with open(imagen): 
                logo_final = QLabel(self); 
                pixmap = QPixmap(imagen); 
                logo_final.setPixmap(pixmap); 
                logo_final.move(25,80); 
        except FileNotFoundError as error: 
            print(f"Imagen no encontrada.\nError: {error}"); 
    
    

if __name__ == '__main__': 
    aplicacion = QApplication(sys.argv); 
    ventana = VentanaConImagen(); 
    sys.exit(aplicacion.exec()); 