from PyQt5.QtWidgets import QApplication
from clases.ventana_bienvenida import VentanaBienvenida
from clases.ventana_test import VentanaTest
from clases.ventana_final import VentanaFinal

if __name__ == "__main__":
    app = QApplication([])  # Se crea la app

    with open("test-de-Ruffier/estilos/estilos.qss", "r") as f:
        app.setStyleSheet(f.read())
        
    ventana = VentanaBienvenida()  # Se instancia la ventana
    ventana.show()    # Se muestra en pantalla

    app.exec_()  # Se ejecuta el loop principal