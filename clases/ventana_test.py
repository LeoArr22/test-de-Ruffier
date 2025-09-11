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
        self.nombre_input.setFixedWidth(200)
        self.edad = QLabel("Ingrese su edad:")
        self.edad_input = QLineEdit()
        self.edad_input.setFixedWidth(80)
        
        #--Instrucciones y P0
        self.instruccion = QLabel(
        "Paso 1:\n"
        "Relájate y cuando estés listo, presiona el botón para comenzar el cronómetro.\n"
        "Este cronómetro contará hasta 15 segundos. Durante ese tiempo,\n"
        "debes contar tus pulsaciones hasta que se complete.\n"
        "Luego, ingresa la cantidad de pulsaciones en el recuadro de texto de abajo (P0)."
        )
        self.cronometro_reposo = QPushButton("Cronómetro 15 segundos de Reposo")
        self.cronometro_reposo.setFixedWidth(200)
        self.p0 = QLabel("Pulsaciones en reposo (P0):")
        self.p0_input = QLineEdit()
        self.p0_input.setFixedWidth(100)
        
        #--Instrucciones y P1
        self.instruccion_sentadillas = QLabel(
        "¡Bien! Ahora debes hacer 30 sentadillas en 45 segundos.\n"
        "Presiona el botón de abajo y sigue el contador; por cada número debes hacer una sentadilla.\n"
        "Una vez llegues a 30 y el contador termine, vuelve a tomar tu pulso durante 15 segundos\n" 
        "y colócalo en el recuadro de abajo (P1)."
        )
        self.contador_sentadillas = QPushButton("Iniciar Contador de Sentadillas")
        self.contador_sentadillas.setFixedWidth(200)    
        self.cronometro_sentadillas = QPushButton("Cronómetro 15 segundos Sentadillas")
        self.cronometro_sentadillas.setFixedWidth(200)
        self.p1 = QLabel("Pulsaciones justo después del ejercicio (P1):")
        self.p1_input = QLineEdit()
        self.p1_input.setFixedWidth(100)
        
        #--Instrucciones y P2
        self.instruccion_recuperacion = QLabel(
        "¡Último paso! Espera un minuto después de terminar las sentadillas.\n"
        "Presiona el botón 'Cronómetro 1 minuto' para iniciar la espera."
        )
        self.cronometro_recuperacion = QPushButton("Cronómetro 1 minuto Descanso")
        self.cronometro_recuperacion.setFixedWidth(200)
        
        self.instruccion_final = QLabel(
        "Para finalizar, pulsa el boton 'Cronometro 15 segundos y toma tu pulso durante ese tiempo.\n" 
        "Coloca la cantidad de pulsasiones en el recuadro de abajo (P2).")
        self.cronometro_recuperacion_final = QPushButton("Cronómetro 15 segundos Recuperación")
        self.cronometro_recuperacion_final.setFixedWidth(200)
        self.p2 = QLabel("Pulsaciones después de un minuto de recuperación (P2):")
        self.p2_input = QLineEdit()
        self.p2_input.setFixedWidth(100)
        
        #Layouts  
        #--Layout Principal
        self.layout_principal = QVBoxLayout()
        
        #--Titulo
        self.layout_principal.addWidget(self.titulo)
        
        #--Nombre y Edad
        self.layout_nombre_edad = QFormLayout()
        self.layout_nombre_edad.addRow(self.nombre, self.nombre_input)
        self.layout_nombre_edad.addRow(self.edad, self.edad_input)
        self.layout_principal.addLayout(self.layout_nombre_edad)
        
        #--Instrucciones y P0
        self.layout_principal.addWidget(self.instruccion)
        self.layout_principal.addWidget(self.cronometro_reposo)   
        self.layout_p0 = QFormLayout()
        self.layout_p0.addRow(self.p0, self.p0_input)
        self.layout_principal.addLayout(self.layout_p0)   
        
        #--Instrucciones y P1 
        self.layout_principal.addWidget(self.instruccion_sentadillas)
        self.layout_principal.addWidget(self.contador_sentadillas)
        self.layout_principal.addWidget(self.cronometro_sentadillas)
        self.layout_p1 = QFormLayout()
        self.layout_p1.addRow(self.p1, self.p1_input)
        self.layout_principal.addLayout(self.layout_p1)
        
        #--Instrucciones y P2
        self.layout_principal.addWidget(self.instruccion_recuperacion)
        self.layout_principal.addWidget(self.cronometro_recuperacion)
        self.layout_principal.addWidget(self.instruccion_final)
        self.layout_principal.addWidget(self.cronometro_recuperacion_final) 
        self.layout_p2 = QFormLayout()
        self.layout_p2.addRow(self.p2, self.p2_input)
        self.layout_principal.addLayout(self.layout_p2)
        
        #-- Set Layout Principal
        self.setLayout(self.layout_principal)
        
        