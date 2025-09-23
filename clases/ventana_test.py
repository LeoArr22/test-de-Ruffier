from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QFormLayout, QMessageBox
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QFont
from clases.ventana_base import VentanaBase
from clases.ventana_final import VentanaFinal

TAM_BOTON = 300

class VentanaTest(VentanaBase):
    def __init__(self):
        super().__init__(titulo="Test de Ruffier", ancho=1000, alto=1000)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.time = None
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
        self.cronometro_reposo = QPushButton("Cronómetro 15 segundos Reposo")
        self.cronometro_reposo.setFixedWidth(TAM_BOTON)
        self.cronometro_reposo.clicked.connect(lambda: self.timer_test(15))
        self.p0 = QLabel("Pulsaciones en reposo (P0):")
        self.p0_input = QLineEdit()
        self.p0_input.setFixedWidth(100)
        
        #--Instrucciones y P1
        self.instruccion_sentadillas = QLabel(
        "¡Bien! Ahora debes hacer 30 sentadillas en 45 segundos.\n"
        "Presiona el botón de abajo y sigue el contador; por cada número debes hacer una sentadilla.\n"
        "Una vez llegues a 30 y el contador termine, vuelve a tomar tu pulso durante 15 segundos\n" 
        "(utiliza el cronometro de 15 segundos Esfuerzo) y colócalo en el recuadro de abajo (P1)."
        )
        self.label_cont_cronometro = QLabel("----------------------")
        self.label_cont_cronometro.setObjectName("cronometro")
        self.contador_sentadillas = QPushButton("Iniciar Contador de Sentadillas")
        self.contador_sentadillas.setFixedWidth(TAM_BOTON)
        self.contador_sentadillas.clicked.connect(lambda: self.timer_test(45, solo_segundos=True))
        self.cronometro_sentadillas = QPushButton("Cronómetro 15 segundos Esfuerzo")
        self.cronometro_sentadillas.setFixedWidth(TAM_BOTON)
        self.cronometro_sentadillas.clicked.connect(lambda: self.timer_test(15))
        self.p1 = QLabel("Pulsaciones justo después del ejercicio (P1):")
        self.p1_input = QLineEdit()
        self.p1_input.setFixedWidth(100)
        
        #--Instrucciones y P2
        self.instruccion_recuperacion = QLabel(
        "¡Último paso! Espera un minuto después de terminar las sentadillas.\n"
        "Presiona el botón 'Cronómetro 1 minuto' para iniciar la espera."
        )
        self.cronometro_recuperacion = QPushButton("Cronómetro 1 minuto Descanso")
        self.cronometro_recuperacion.setFixedWidth(TAM_BOTON)
        self.cronometro_recuperacion.clicked.connect(lambda: self.timer_test(60))
        
        self.instruccion_final = QLabel(
        "Para finalizar, pulsa el boton 'Cronometro 15 segundos y toma tu pulso durante ese tiempo.\n" 
        "Coloca la cantidad de pulsasiones en el recuadro de abajo (P2).")
        self.cronometro_recuperacion_final = QPushButton("Cronómetro 15 segundos Recuperación")
        self.cronometro_recuperacion_final.setFixedWidth(TAM_BOTON)
        self.cronometro_recuperacion_final.clicked.connect(lambda: self.timer_test(15))
        self.p2 = QLabel("Pulsaciones después de un minuto de recuperación (P2):")
        self.p2_input = QLineEdit()
        self.p2_input.setFixedWidth(100)
        
        self.boton_continuar = QPushButton("Continuar")
        
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
        self.layout_horizontal = QHBoxLayout()
        self.layout_horizontal.addWidget(self.instruccion_sentadillas)
        self.layout_horizontal.addWidget(self.label_cont_cronometro, alignment=Qt.AlignCenter)
        self.layout_principal.addLayout(self.layout_horizontal)
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
        self.layout_principal.addWidget(self.boton_continuar, alignment=Qt.AlignCenter)
        self.boton_continuar.clicked.connect(self.mostrar_ventana_final)
        #-- Set Layout Principal
        self.setLayout(self.layout_principal)
        
    def timer_test(self, segundos, solo_segundos=False):
        """Inicia un cronómetro genérico con segundos indicados."""
        # Reiniciar tiempo
        self.solo_segundos = solo_segundos
        self.time = QTime(0, segundos // 60, segundos % 60)

        # Mostrar el tiempo inicial
        if self.solo_segundos:
            self.label_cont_cronometro.setText(self.time.toString("ss"))
        else:    
            self.label_cont_cronometro.setText(self.time.toString("mm:ss"))

        # Reiniciar el timer
        if self.timer.isActive():
            self.timer.stop()
        self.timer.start(1000)


    def update_timer(self):
        """Se llama cada segundo para actualizar la pantalla."""
        self.time = self.time.addSecs(-1)
        
        if self.solo_segundos:
            self.label_cont_cronometro.setText(self.time.toString("ss"))
        else:    
            self.label_cont_cronometro.setText(self.time.toString("mm:ss"))

        # Cuando llega a cero, parar
        if self.time == QTime(0, 0, 0):
            self.timer.stop()
            
    def mostrar_ventana_final(self):
        datos = self.validar_inputs()
        if datos:  # Solo continua si la validación pasó
            self.test = VentanaFinal(datos)
            self.test.show()
            self.close()
            
    def validar_inputs(self):
        """
        Valida los campos de entrada de la ventana de test.
        Retorna un diccionario con los datos si son válidos, o None si falla.
        """
        nombre = self.nombre_input.text().strip()
        edad = self.edad_input.text().strip()
        p0 = self.p0_input.text().strip()
        p1 = self.p1_input.text().strip()
        p2 = self.p2_input.text().strip()

        if not nombre:
            self.mostrar_error("Debe ingresar un nombre")
            return None

        if not edad.isdigit():
            self.mostrar_error("La edad debe ser un número entero")
            return None

        for i, valor in zip(["P0", "P1", "P2"], [p0, p1, p2]):
            if not valor.isdigit():
                self.mostrar_error(f"El valor de {i} debe ser un número entero")
                return None

        return {
            "nombre": nombre,
            "edad": int(edad),
            "p0": int(p0),
            "p1": int(p1),
            "p2": int(p2)
        }

    def mostrar_error(self, mensaje):
        QMessageBox.warning(self, "Error de validación", mensaje)

                
        