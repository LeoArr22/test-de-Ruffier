from PyQt5.QtWidgets import QVBoxLayout, QLabel, QPushButton
from clases.ventana_base import VentanaBase
from clases.ventana_test import VentanaTest
from recursos.instrucciones import ventana_bienvenida

class VentanaBienvenida(VentanaBase):
    def __init__(self):
        super().__init__(titulo="Bienvenida", alto=400, ancho=600)
        #widgets
        self.bienvenida = QLabel(ventana_bienvenida['bienvenida'])
        self.explicacion_texto = QLabel(ventana_bienvenida['explicacion'])
        
        self.comenzar = QPushButton("Comenzar")
        self.comenzar.clicked.connect(self.mostrar_ventana_test)

        self.layout = QVBoxLayout()
        
        self.layout.addWidget(self.bienvenida)
        self.layout.addWidget(self.explicacion_texto)
        self.layout.addWidget(self.comenzar)
        
        self.setLayout(self.layout)

    def mostrar_ventana_test(self):
        self.test = VentanaTest()  # crea la ventana secundaria
        self.test.show()
        self.close()  # cerrar la ventana principal
