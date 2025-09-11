from PyQt5.QtWidgets import QWidget

class VentanaBase(QWidget):
    def __init__(self, titulo="Ventana", ancho=800, alto=600):
        super().__init__()
        self.setWindowTitle(titulo)
        self.setFixedSize(ancho, alto)
        self.centrar()

    def centrar(self):
        """Centra la ventana en la pantalla"""
        pantalla = self.screen().geometry()
        x = (pantalla.width() - self.width()) // 2
        y = (pantalla.height() - self.height()) // 2
        self.move(x, y)