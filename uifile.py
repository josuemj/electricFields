from IPython.external.qt_for_kernel import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import uic
from matplotlib.figure import Figure

import numpy as np

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from pyqt5_plugins.examplebutton import QtWidgets
def f(x, R):
    return np.sqrt(np.maximum(0, R**2 - 9 * x**2))

def h(x, R):
    return -np.sqrt(np.maximum(0, R**2 - 9 * x**2))

class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI,self).__init__()
        uic.loadUi("interface.ui",self)

        self.pushButton.clicked.connect(self.campoElectrico)


        # combo_box
        self.fieldsComboBox.addItem("Anillo")
        self.fieldsComboBox.addItem("Disco")
        self.fieldsComboBox.addItem("Linea")

        #Sliders

        #radioSlider
        self.radioSlider.setMinimum(0)
        self.radioSlider.setMaximum(100)
        self.radioSlider.setValue(50)  # Initial value
        self.radioSlider.setTickPosition(QSlider.TicksBothSides)

        #x-axisSlider
        self.xSlider.setMinimum(0)
        self.xSlider.setMaximum(100)
        self.xSlider.setValue(50)  # Initial value
        self.xSlider.setTickPosition(QSlider.TicksBothSides)

        #graph
        fig, ax = plt.subplots()

        # Example data (replace with your own)
        #x = [-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6]
        #y = [0,0,0,0,0,0,0,0,0,0,0,0,0]
        x = np.linspace(-4, 4, 1000)
        R = 3

        ax.plot(x, f(x, R), color='blue')
        ax.plot(x, h(x, R), color='blue')

        # Plot the data
        ax.set_xlabel('X (m)')
        ax.set_ylabel('Y (m)')
        ax.set_title('Matplotlib Graph')

        canvas = FigureCanvas(fig)
        layout = self.graphFrame.layout()

        new_layout = QVBoxLayout(self.graphFrame)
        new_layout.addWidget(canvas)




        self.show()

    def campoElectrico(self):
        print("Button has been pressed")
        selected_item_text = self.fieldsComboBox.currentText()
        print("Selected figure: "+selected_item_text)

        if selected_item_text == "Anillo":
            print("Anillo seleccionado")

        if selected_item_text == "Disco":
            print("Disco seleccionado")

        if selected_item_text == "Linea":
            print("Linea seleccionada")






def main():
    print("Running applicatio")
    app = QApplication([])
    window = MyGUI()
    app.exec_()

if __name__ == "__main__":
    main()




