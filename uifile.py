from IPython.external.qt_for_kernel import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import uic
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from Ejercicio5 import*


"""""""""""""""""""""""""""""""""""""""""""""""""""""
====== FUNCIONES MATEAMÁTICAS PARA GRAFICAR =========
"""""""""""""""""""""""""""""""""""""""""""""""""""""

def f(x, R):
    return (R/0.5)*(np.sqrt(np.maximum(0, 0.5**2 - x**2)))

def h(x, R):
    return -(R/0.5)*(np.sqrt(np.maximum(0, 0.5**2 - x**2)))

def j(x):
    return x**2

def rectaNegativa(x,radio_intercepto_y,intercepto_x):
    return(-radio_intercepto_y/intercepto_x)*x+radio_intercepto_y

def rectaPositiva(x,radio_intercepto_y,intercepto_x):
    return(radio_intercepto_y/intercepto_x)*x-radio_intercepto_y


"""""""""""""""""""""""""""""""""""""""""""""""""""""
============== CREACION DE INTERRFAZ ===============
"""""""""""""""""""""""""""""""""""""""""""""""""""""

class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI,self).__init__()
        uic.loadUi("interface.ui",self)

        self.pushButton.clicked.connect(self.campoElectrico)
        self.radioSlider.valueChanged.connect(self.updateRadioLabel)
        self.xSlider.valueChanged.connect(self.updatePosicionLabel)


        """""""""""""""""""""""""""""""""""""""""""""""""""""""""
        #================= Componentes por defecto ==============
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""
        # combo_box
        self.fieldsComboBox.addItem("Anillo")
        self.fieldsComboBox.addItem("Disco")
        self.fieldsComboBox.addItem("Linea")

        #Sliders

        #radioSlider
        self.radioSlider.setMinimum(1)
        self.radioSlider.setMaximum(10)
        self.radioSlider.setValue(5)  # Initial value
        self.radioSlider.setTickPosition(QSlider.TicksBothSides)

        #x-axisSlider
        self.xSlider.setMinimum(1)
        self.xSlider.setMaximum(100)
        self.xSlider.setValue(50)  # Initial value
        self.xSlider.setTickPosition(QSlider.TicksBothSides)

        """
        ================= Grafico por defecto ==================
        """
        fig, ax = plt.subplots()
        x = [-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6]
        y = [0,0,0,0,0,0,0,0,0,0,0,0,0]
        ax.plot(x,y,color='blue')
        ax.set_title('Campo eléctrico')

        canvas = FigureCanvas(fig)
        layout = self.graphFrame.layout()

        new_layout = QVBoxLayout(self.graphFrame)
        new_layout.addWidget(canvas)

        #Mostrar pantalla
        self.show()

    def campoElectrico(self):

        print("Button has been pressed") #Control
        selected_item_text = self.fieldsComboBox.currentText()
        print("Selected figure: "+selected_item_text)

        radio = int(self.radioSlider.value())
        print("Valor actual del radio"+str(radio)) #Control

        posicion_x = int(self.xSlider.value())
        print("posicion en x(m)" + str(posicion_x)) #Control



        if selected_item_text == "Anillo":
            print("Anillo seleccionado") #Control
            self.graficarAnillo(radio,posicion_x)

        if selected_item_text == "Disco":
            print("Disco seleccionado") #Control
            self.graficarDicos(radio,posicion_x)

        if selected_item_text == "Linea":
            print("Linea seleccionada") #Control
            self.graficarLinea(radio,posicion_x)

    def graficarAnillo(self,r,posicion_x):

        self.clearGraphFrame() #Limpiando el grafico anterior
        puntoP = "(0,"+str(posicion_x)+")"

        x = np.linspace(-0.5,0.5, 1000) #Dominio de la elipse
        dominioRecta = np.linspace(0,posicion_x,1000) #Dominio de la recta
        fig, ax = plt.subplots()

        ax.plot(x, f(x, r), color='blue')
        ax.plot(x, h(x, r), color='blue')

        #rectas al punto P
        ax.plot(dominioRecta, rectaNegativa(dominioRecta,r,posicion_x))
        ax.plot(dominioRecta, rectaPositiva(dominioRecta, r, posicion_x))

        plt.scatter(posicion_x, 0, color='red', zorder=2)
        plt.text(posicion_x, 2, puntoP, fontsize=16, color='black')

        ax.set_title('Campo eléctrico de anillo')
        ax.grid(True)

        canvas = FigureCanvas(fig)
        layout = self.graphFrame.layout()
        layout.addWidget(canvas)

        campo_anillo = anillo(posicion_x,r)
        print("Campo anillo "+str(campo_anillo))

        self.campoLabel.setText("Campo eléctrico "+str(campo_anillo)+ " N/C")

    def graficarDicos(self,r,posicion_x):

        self.clearGraphFrame()
        puntoP = "(0," + str(posicion_x) + ")"

        x = np.linspace(-0.5, 0.5, 1000)  # Dominio de la elipse
        dominioRecta = np.linspace(0, posicion_x, 1000)  # Dominio de la recta
        fig, ax = plt.subplots()

        # Customize the plot for "Anillo"
        ax.plot(x, f(x, r), color='blue')
        ax.plot(x, h(x, r), color='blue')
        ax.fill_between(x, f(x, r), h(x, r), color='blue', alpha=0.3)

        # rectas al punto P
        ax.plot(dominioRecta, rectaNegativa(dominioRecta, r, posicion_x))
        ax.plot(dominioRecta, rectaPositiva(dominioRecta, r, posicion_x))

        plt.scatter(posicion_x, 0, color='red', zorder=2)
        plt.text(posicion_x, 2, puntoP, fontsize=16, color='black')
        ax.set_title('Campo eléctrico disco')
        ax.grid(True)

        canvas = FigureCanvas(fig)
        layout = self.graphFrame.layout()
        layout.addWidget(canvas)

        campo_disco = disco(posicion_x,r)
        print("campo electrico Disco: "+str(campo_disco))
        self.campoLabel.setText("Campo eléctrico " + str(campo_disco) + " N/C")


    def graficarLinea(self,r,posicion_x):
        self.clearGraphFrame()
        puntoP = "(0," + str(posicion_x) + ")"
        dominioRecta = np.linspace(0, posicion_x, 1000)  # Dominio de la recta


        fig, ax = plt.subplots()
        ax.plot([0, 0], [r, -r], color='b', linestyle='-', marker='o')
        ax.plot(dominioRecta, rectaNegativa(dominioRecta, r, posicion_x))
        ax.plot(dominioRecta, rectaPositiva(dominioRecta, r, posicion_x))
        ax.text(posicion_x-0.2, 1.2, puntoP, fontsize=16, color='black')

        ax.scatter([0, 0], [r, -r], color='r', label='Puntos')
        ax.grid(True)
        ax.scatter(posicion_x, 0, color='red', zorder=2)

        ax.set_title('Campo eléctro linea')
        canvas = FigureCanvas(fig)
        layout = self.graphFrame.layout()
        layout.addWidget(canvas)

        campoLinea = lineal(r*2,posicion_x) #Valor campo electrico
        self.campoLabel.setText("Campo eléctrico "+str(campoLinea)+" N/C")



    def clearGraphFrame(self):
        # Remove all widgets from the graphFrame layout
        layout = self.graphFrame.layout()
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

    def updateRadioLabel(self, value):
        self.radioLabel.setText(str(value)+"m")


    def updatePosicionLabel(self, value):
        self.posicionLabel.setText(str(value)+"m")

"""
====================== START ===========================
"""

def main():
    print("Running applicatio")
    app = QApplication([])
    window = MyGUI()
    app.exec_()

if __name__ == "__main__":
    main()



