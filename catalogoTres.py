import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit)
from PyQt6.QtGui import QFont
from PyQt6.QtGui import QPixmap; 


class VentanaConImagen(QWidget): 

    def __init__(self): 
        super().__init__(); 
        self.iniciarUI(); 

    def iniciarUI(self): 
        self.setGeometry(500,300,440,220)
        self.setWindowTitle("Fashion Store"); 
        self.configurarVentanaConImagen(); 
        self.show(); 

    def configurarVentanaConImagen(self): 
        QLabel (" CHAQUETA ABRIGADA ", self).move(30,5) 
        mensaje_rotulo = QLabel(self);  
        mensaje_rotulo.setText("Nueva Chaqueta De Abrigo \nTamaño De Los Hombres \nAl Aire Libre Equitación \n De GranUniforme De Béisbol"); 
        mensaje_rotulo.move(20,60); 
        imagen = "img/tress.png"; 
        boton_adquirir = QPushButton("Adquirir", self)
        boton_adquirir.move(60,170)
        try: 
            with open(imagen): 
                Fashion_Store = QLabel(self); 
                pixmap = QPixmap(imagen); 
                pixmap.width=50
                Fashion_Store.setPixmap(pixmap); 
                Fashion_Store.move(220,1); 
        except FileNotFoundError as error: 
            print(f"Imagen no encontrada.\nError: {error}"); 

        
        
if __name__ == '__main__': 
    aplicacion = QApplication(sys.argv); 

    ventana = VentanaConImagen(); 

    sys.exit(aplicacion.exec()); 
    
    