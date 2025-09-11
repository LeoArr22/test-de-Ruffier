from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QFormLayout
from PyQt5.QtCore import QTimer
from clases.ventana_base import VentanaBase

class VentanaTest(VentanaBase):
    def __init__(self):
        super().__init__(titulo="Test de Ruffier")
        #widgets
        
        #--Titulo
        self.titulo = QLabel("Test de Ruffier")

        #--Nombre y Edad
        self.nombre = QLabel("Ingrese su nombre:")
        self.nombre_input = QLineEdit()
        self.edad = QLabel("Ingrese su edad:")
        self.edad_input = QLineEdit()
        
        #--Instrucciones y P0
        self.instruccion = QLabel(
        "Paso 1:\n"
        "Relájate y cuando estés listo, presiona el botón para comenzar el cronómetro.\n"
        "Este cronómetro contará hasta 15 segundos. Durante ese tiempo, "
        "debes contar tus pulsaciones hasta que se complete."
        "Luego, ingresa la cantidad de pulsaciones en el recuadro de texto de abajo."
        )
        self.cronometro_reposo = QPushButton("Iniciar Cronómetro 15 segundos")
        self.p0 = QLabel("Pulsaciones en reposo (P0):")
        self.p0_input = QLineEdit()
        
        #--Instrucciones y P1
        self.instruccion_sentadillas = QLabel("""¡Bien!
        Ahora debes hacer 30 sentadillas en 45 segundos.
        Presiona el botón de abajo y sigue el contador; por cada número debes hacer una sentadilla.
        Una vez llegues a 30 y el contador termine, vuelve a tomar tu pulso durante 15 segundos 
        y colócalo en el recuadro de abajo.
        """)
        self.contador_sentadillas = QPushButton("Iniciar Contador")
        self.p1 = QLabel("Pulsaciones justo después del ejercicio (P1):")
        self.p1_input = QLineEdit()
        
        #--Instrucciones y P2
        self.instruccion_recuperacion = QLabel("""¡Último paso!
        Espera un minuto después de terminar las sentadillas.
        Presiona el botón 'Cronómetro 1 minuto' para iniciar la espera.""")
        self.cronometro_recuperacion = QPushButton("Cronómetro 1 minuto")
        
        self.instruccion_final = QLabel("""Para finalizar, pulsa el boton 'Cronometro 15 segundos' 
        y toma tu pulso durante ese tiempo.
        Coloca la cantidad de pulsasiones en el recuadro de abajo.""")
        self.p2 = QLabel("Pulsaciones después de un minuto de recuperación (P2):")
        self.p2_input = QLineEdit()
        
        #-- Contador/Cronometro
        self.crono_conta = QTimer()
        
        #Layouts
        #--Titulo
        self.lineh1 = QHBoxLayout()
        self.lineh1.addWidget(self.titulo)
        #--Nombre y Edad
        self.layout_form = QFormLayout()
        self.layout_form.addRow(self.nombre, self.nombre_input)
        self.layout_form.addRow(self.edad, self.edad_input)
        #--Instrucciones y P0
        self.lineh2 = QHBoxLayout()
        self.lineh2.addWidget(self.instruccion)
        self.lineh2.addWidget(self.cronometro_reposo)   
        self.layout_p0 = QFormLayout()
        self.layout_p0.addRow(self.p0, self.p0_input)   
        #--Instrucciones y P1
        self.lineh3 = QHBoxLayout() 
        self.lineh3.addWidget(self.instruccion_sentadillas)
        self.lineh3.addWidget(self.contador_sentadillas)
        self.layout_p1 = QFormLayout()
        self.layout_p1.addRow(self.p1, self.p1_input)
        #--Instrucciones y P2
        self.lineh4 = QHBoxLayout()
        self.lineh4.addWidget(self.instruccion_recuperacion)
        self.lineh4.addWidget(self.cronometro_recuperacion)
        self.layout_p2 = QFormLayout()
        self.layout_p2.addRow(self.p2, self.p2_input)
        self.lineh5 = QHBoxLayout()
        self.lineh5.addWidget(self.instruccion_final)
        #--Layout Principal
        self.layout = QVBoxLayout()
        self.layout.addLayout(self.lineh1)
        self.layout.addLayout(self.layout_form)
        self.layout.addLayout(self.lineh2)
        self.layout.addLayout(self.layout_p0)
        self.layout.addLayout(self.lineh3)
        self.layout.addLayout(self.layout_p1)
        self.layout.addLayout(self.lineh4)
        self.layout.addLayout(self.layout_p2)
        self.layout.addLayout(self.lineh5)
        self.setLayout(self.layout)
        
        