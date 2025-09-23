from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QFormLayout
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QFont
from clases.ventana_base import VentanaBase

class VentanaFinal(VentanaBase):
    def __init__(self, datos, titulo="Resultados", ancho=800, alto=600):
        super().__init__(titulo, ancho, alto)
        self.datos = datos
        self.index=(4*(int(self.datos["p0"])+int(self.datos["p1"])+int(self.datos["p2"]))-200)/10
        txt_res1 = "bajo. ¡Acuda al médico de inmediato!"
        txt_res2 = "satisfactorio. ¡Vea a su médico!"
        txt_res3 = "promedio. Puede valer la pena ver a su médico para que lo revise."
        txt_res4 = "por encima del promedio"
        txt_res5 = "alto"

        if datos["edad"] >= 15:
            if self.index >= 15:
                mensaje = txt_res1
            elif self.index >= 11 and self.index <= 14.9:
                mensaje = txt_res2
            elif self.index >= 6 and self.index <= 10.9:
                mensaje = txt_res3
            elif self.index > 0.5 and self.index <= 5.9:
                mensaje = txt_res4
            else:
                mensaje = txt_res5
        elif datos["edad"] == 13 or datos["edad"] == 14:
            if self.index >= 15:
                mensaje = txt_res1
            elif self.index >= 11 and self.index <= 14.9:
                mensaje = txt_res2
            elif self.index >= 6 and self.index <= 10.9:
                mensaje = txt_res3
            elif self.index > 0.5 and self.index <= 5.9:
                mensaje = txt_res4
            else:
                mensaje = txt_res5
        
        #widgets
        self.indice = QLabel(f"Indice de Ruffier: {self.index}") 
        self.perfomance = QLabel(f"Rendimiento Cardiaco: {mensaje}")
        self.boton_reiniciar = QPushButton("Reiniciar Test")
        self.boton_reiniciar.clicked.connect(self.reiniciar)
        
        #Layout
        self.layout_principal = QVBoxLayout()
        self.layout_principal.addWidget(self.indice)
        self.layout_principal.addWidget(self.perfomance)
        self.layout_principal.addWidget(self.boton_reiniciar)
        self.setLayout(self.layout_principal)
        
    def reiniciar(self):
        from clases.ventana_bienvenida import VentanaBienvenida
        self.v1 = VentanaBienvenida()  # crea una nueva instancia de la primera
        self.v1.show()
        self.close()