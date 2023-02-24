from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from name import Store


class Catalogos(QWidget):
    
    def __init__(self, image_list):
        super().__init__()
        self.image_list = image_list
        self.current_image = 0
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("Escoge tu producto")
        self.setStyleSheet("background-color: white;")
        self.setFixedSize(450, 210)

        # image label
        self.image_label = QLabel(self)
        self.image_label.setStyleSheet("border: 2px solid #000000;")

        # next button
        next_button = QPushButton('Next', self)
        next_button.setStyleSheet('background-color: #C8FF9D;')
        next_button.setGeometry(240, 120, 100, 30)
        next_button.clicked.connect(self.next_image)

        # buy button
        buy_button = QPushButton('Comprar', self)
        buy_button.setGeometry(350, 120, 80, 30)
        buy_button.setStyleSheet('background-color: #AEF8F0;')
        buy_button.clicked.connect(self.abrirOtroModulo)

        # text label
        self.text_label = QLabel(self)
        self.text_label.setStyleSheet("font-size: 11px;color: #00000; padding: 10px;")
        self.text_label.setGeometry(240, 20, 190, 80)
        self.text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.show_image()

    def show_image(self):
        pixmap = QPixmap(self.image_list[self.current_image][0])
        self.image_label.setPixmap(pixmap)
        self.image_label.setGeometry(0, 0, pixmap.width(), pixmap.height())

        self.update_text_label()

    def next_image(self):
        self.current_image = (self.current_image + 1) % len(self.image_list)
        self.show_image()

    def update_text_label(self):
        self.text_label.setText(self.image_list[self.current_image][1])
    
    def abrirOtroModulo(self):
        # aquí iría el código para abrir el otro módulo
        self.hide()  # Oculta la ventana actual
        self.otro_modulo = Store()  # Inicializa el nuevo módulo
        self.otro_modulo.show()  # Muestra el nuevo módulo
        print('comprado!')
       

if __name__ == '__main__':
    app = QApplication([])

    # slider img
    image_list = [
        ('img/tress.png', 'Nueva Chaqueta De Abrigo \nTamaño De Los Hombres \nAl Aire Libre Equitación \nDe Gran Uniforme De Béisbol'),
        ('img/dos.png', 'Saco de invierno \nCallejera Hombres Cuello \nRedondo Camiseta De \nManga Larga'),
        ('img/unoooo.png', 'Nueva Camiseta De Manga \nCorta Para Hombres Hip Hop'),
        ('img/tress.png', 'Nueva Chaqueta De Abrigo \nTamaño De Los Hombres \nAl Aire Libre Equitación \nDe Gran Uniforme De Béisbol')
    ]

    image_slider = Catalogos(image_list)
    image_slider.show()

    app.exec()
